

def rectangle_intersections(x1, x2, y1, y2, a1, a2, b1, b2):
    """Checks two proper, non-rotated rectangles for points of intersection"""

    # comparison only works if coordinates in ascending order
    if x1 > x2:
        x1, x2, = x2, x1
    if y1 > y2:
        y1, y2, = y2, y1
    if a1 > a2:
        a1, a2, = a2, a1
    if b1 > b2:
        b1, b2, = b2, b1

    # check if same rectangle
    if x1 == a1 and x2 == a2 and y1 == b1 and y2 == b2:
        return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]

    intersections = []

    # check line on y1
    intersections.extend(intersect(x1, x2, y1, a1, a2, b1, b2))
    # check line on y2
    intersections.extend(intersect(x1, x2, y2, a1, a2, b1, b2))
    # check line on x1
    intersections.extend(intersect(y1, y2, x1, b1, b2, a1, a2, False))
    # check line on x2
    intersections.extend(intersect(y1, y2, x2, b1, b2, a1, a2, False))

    return intersections if intersections else 0


def intersect(x1, x2, y, a1, a2, b1, b2, horizontal=True):
    """Checks a line of XY for intersections with the perpendicular lines of AB"""
    intersections = []

    # check if ab can overlap with line (x1, y), (x2, y) vertically
    if b1 <= y <= b2:
        # check if line (a1, b1), (a1, b2) overlaps horizontally
        if x1 <= a1 <= x2:
            if horizontal:
                intersections.append((a1, y))
            else:
                intersections.append((y, a1))
        # check if line (a2, b1), (a2, b2) overlaps horizontally
        if x1 <= a2 <= x2:
            if horizontal:
                intersections.append((a2, y))
            else:
                intersections.append((y, a2))

    return intersections



