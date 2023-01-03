def main(a, b, c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b:
        if a > c:
            return a
        return c
    if b > a:
        if b > c:
            return b
        return c
    return


print(main(6, 7, 9))
