def main(a, b, c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b and b > c or c > b and b > a:
        return b
    if b > c and c > a or a > c and c > b:
        return c
    else:
        return a


print(main(1, 9, 5))
