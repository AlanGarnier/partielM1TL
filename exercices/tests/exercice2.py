# Function to test with doctest
def divide(x, y):
    """
        Cette fonction effectue une addition de deux nombres.

        Exemples:
        >>> divide(8, 4)
        2.0
        >>> divide(2, 2)
        1.0
        >>> divide(5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
        """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


# Launch this command in terminal : python -m doctest -v exercice2.py
if __name__ == "__main__":
    import doctest

    doctest.testmod()
