print("Hello, World!")
#mean function
def mean(numbers):
    return sum(numbers) / len(numbers)
# Example usage
numbers = [1, 2, 3, 4, 5]
print("Mean:", mean(numbers))
#median function
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
    #median function
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
# Example usage
numbers = [1, 2, 3, 4, 5]
print("Median:", median(numbers))