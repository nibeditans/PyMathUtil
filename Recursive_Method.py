# Recursion
def factorial_recursive(n):
    """

    :param n: integer
    :return: n * (n-1) * (n-2) * ... * 3 * 2 * 1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter the number: "))
print("Factorial using Recursive method:", factorial_recursive(number))