def get_geometric_mean(*nums: float) -> float:
    """
    Calculate the geometric mean of a sequence of numbers
    """

    if len(nums) == 0:
        raise ValueError("Sequence cannot be empty")

    product = 1
    for num in nums:
        product *= num

    return product ** (1 / len(nums))


# Example test
print(get_geometric_mean(5, 20))
print(get_geometric_mean(5, 20, 10))