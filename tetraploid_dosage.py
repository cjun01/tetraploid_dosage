from math import comb

def calculate_probabilities(a, b):
    # Probabilities from heuristic
    # 0:AAAA, 1:AAAB,2:AABB,3:ABBB,4:BBBB
    p_values = {
        0: 1,  # Placeholder value, modify as necessary
        1: 3 / 4,
        2: 2 / 4,
        3: 1 / 4,
        4: 0  # Placeholder value, modify as necessary
    }

    # Calculate binomial probability
    def binomial_probability(n, k, p):
        return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    n = a + b

    # Check for the special cases
    if a == 0 and b == 0:
        print("No reads.")
        return
    if a == 0:
        probabilities = {4: 1}
    elif b == 0:
        probabilities = {1: 1}
    else:
        # Compute probabilities for each scenario
        probs = {}
        for dosage, p in p_values.items():
            probs[dosage] = binomial_probability(n, a, p)

            if probs[dosage] > 1:
                probs[dosage] = 0
            if probs[dosage] < 0:
                probs[dosage] = 0

        # Normalize the probabilities
        total_prob = sum(probs.values())
        probabilities = {k: v / total_prob for k, v in probs.items()}

    # Check if there are reads or not
    if not probabilities:
        print("No reads.")
        return

    # Print the probabilities for all dosage categories
    for dosage, prob in probabilities.items():
        print(f"Dosage = {dosage}: Probability = {prob:.4f}")

    return probabilities
