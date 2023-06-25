def sum_of_digits(number):
    digit_sum = 0
    while number != 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    return digit_sum

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate the sum of digits
result = sum_of_digits(number)

# Print the sum of digits
print("The sum of digits in", number, "is", result)
