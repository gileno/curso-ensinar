def fatorial(n):
    """Return fatorial of n

    >>> fatorial(5)
    120
    >>> [fatorial(i) for i in (1, 2, 3, 4)]
    [1, 2, 6, 24]
    >>> fatorial(-10)
    Traceback (most recent call last):
      ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    elif n <= 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
