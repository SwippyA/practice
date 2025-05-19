def generate_series_1(a: int) -> str:
    if a < 1:
        return "Input must be a positive integer"
    
    series = [str(2*i + 1) for i in range(a)]
    return ", ".join(series)

# Example usage:
print(generate_series_1(1))  # Output: "1"
print(generate_series_1(4))  # Output: "1, 3, 5, 7"