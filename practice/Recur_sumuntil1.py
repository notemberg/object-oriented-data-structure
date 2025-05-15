def sum_until_single_digit(n):
    n = abs(n)  # Take the absolute value to ignore any negative sign
    if n < 10:
        return n
    else:
        sum_digits = sum(int(digit) for digit in str(n))
        return sum_until_single_digit(sum_digits)

# Example usage
number = -123456
result = sum_until_single_digit(number)
print(f"The single unit sum of {number} is {result}")