from functools import reduce


# Incorrect implementation (in the book)
def get_geometric_mean_for_three_numbers(a, b, c):
    # FIX: cube root instead of square root
    return (a * b * c) ** (1 / 3)


def get_geometric_mean(*nums: float) -> float:
    """
    Get the geometric mean of a sequence of numbers
    """

    if not len(nums):
        raise ValueError("Cannot calculate the geometric mean of an empty sequence")

    product = reduce(lambda a, b: a * b, nums)

    if product < 0 and len(nums) % 2 == 0:
        raise ValueError("Cannot calculate the geometric mean")

    return pow(product, 1 / len(nums))


# Test
print(get_geometric_mean_for_three_numbers(5, 20, 10))
print(get_geometric_mean(5, 20, 10))