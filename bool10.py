import math
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b=math.sqrt(a)//1
    return b*b==a
print(main(16))    