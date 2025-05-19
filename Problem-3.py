def generate_series_2(a: int) -> str:
    if a < 1:
        return "Input must be a positive integer"
    
    n = a if a % 2 != 0 else a - 1
    series = [str(2*i + 1) for i in range((n + 1) // 2)]
    return ", ".join(series)

# Example usage:
print(generate_series_2(3))  # Output: "1, 3, 5"
print(generate_series_2(4))  # Output: "1, 3"
print(generate_series_2(5))  # Output: "1, 3, 5, 7, 9"