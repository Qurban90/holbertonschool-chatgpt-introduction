#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description: Calculates the factorial of a number using recursion.
    
    Parameters:
    n: Integer number to calculate factorial of.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
