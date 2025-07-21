#Functions & modules
# #task 1
n = int(input("Enter a number : "))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
print(f"Factorial of {n} is", factorial(n))

#task 2
import math

# Function to calculate the square root
def calculate_square_root(num):
    return math.sqrt(num)

# Function to calculate the natural logarithm (base e)
def calculate_log(num):
    if num > 0:
        return math.log(num)
    else:
        return "Undefined (logarithm is only defined for positive numbers)"

# Function to calculate sine of the number (in radians)
def calculate_sine(num):
    return math.sin(num)

# Main function to call the above functions
def main():
    number = int(input("Enter a number: "))  # Sample input

    sqrt_result = calculate_square_root(number)
    log_result = calculate_log(number)
    sine_result = calculate_sine(number)

    print(f"Number: {number}")
    print(f"Square root: {sqrt_result}")
    print(f"Natural logarithm (ln): {log_result}")
    print(f"Sine (in radians): {sine_result}")

# Run the program
main()
