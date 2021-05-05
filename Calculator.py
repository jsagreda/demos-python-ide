a = 6
b = 3
c = 5


def calculate_sum():
    result = a + b + c

    print("Sum of a, b, c is", result)

    if result < 10:
        print("The sum < 10")
    else:
        print("The sum is", result, ">= 10")

# Calculate

calculate_sum()