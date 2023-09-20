# Function to calculate the weighted average
def weighted_average(numbers, weights):
    if len(numbers) != len(weights):
        raise ValueError("The number of numbers and weights must be the same.")
    
    total_weight = sum(weights)
    weighted_sum = sum([num * weight for num, weight in zip(numbers, weights)])
    
    return weighted_sum / total_weight

# Input numbers and their corresponding weights
numbers = [5, 7, 9]
weights = [0.3, 0.4, 0.3]

# Calculate the weighted average
result = weighted_average(numbers, weights)

# Print the weighted average
print("Weighted Average:", result)
