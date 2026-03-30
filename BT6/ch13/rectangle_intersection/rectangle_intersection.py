def rect_intersection_area(rect1, rect2):
    """
    Calculate the intersection area of two rectangles.

    Each rectangle is represented as a tuple:
        (x1, y1, x2, y2)
    where:
        (x1, y1) is bottom-left
        (x2, y2) is top-right

    Raises:
        ValueError: If any rectangle is invalid (zero or negative width/height)

    Returns:
        int/float: Intersection area
    """

    def validate(rect):
        x1, y1, x2, y2 = rect
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle with zero or negative area")

    # Validate both rectangles
    validate(rect1)
    validate(rect2)

    x1_1, y1_1, x2_1, y2_1 = rect1
    x1_2, y1_2, x2_2, y2_2 = rect2

    # Compute overlap boundaries
    inter_left = max(x1_1, x1_2)
    inter_right = min(x2_1, x2_2)
    inter_bottom = max(y1_1, y1_2)
    inter_top = min(y2_1, y2_2)

    # Compute width and height of intersection
    width = inter_right - inter_left
    height = inter_top - inter_bottom

    # If no overlap or just touching → area = 0
    if width <= 0 or height <= 0:
        return 0

    return width * height