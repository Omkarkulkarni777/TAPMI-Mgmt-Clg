def karatsuba_square(x):
    if x < 10:
        return x ** 2

    m = len(str(x)) // 2
    a = x // 10 ** m #floor value
    b = x % (10 ** m) #remainder

    a_squared = karatsuba_square(a)
    b_squared = karatsuba_square(b)
    ab_squared = karatsuba_square(a + b) - a_squared - b_squared

    return a_squared * 10 ** (2 * m) + ab_squared * 10 ** m + b_squared

if __name__ == "__main__":
    try:
        large_integer = int(input("Enter a positive integer: "))
        if large_integer > 0:
            result = karatsuba_square(large_integer)
            print(f"The square of the integer is: {result}")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
