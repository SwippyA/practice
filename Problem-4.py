def count_multiples(numbers: list) -> dict:
    result = {}
    for i in range(1, 10):
        count = sum(1 for num in numbers if num % i == 0)
        result[i] = count
    return result

# Example usage:
print(count_multiples([1,2,8,9,12,46,76,82,15,20,30]))
# Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}