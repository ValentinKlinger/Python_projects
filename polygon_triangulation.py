import numpy as np


def is_ear(polygon, i, direction):
    """
    Determines whether three points form an ear.
    """
    prev_idx = (i - 1) % len(polygon)
    next_idx = (i + 1) % len(polygon)

    prev_point = polygon[prev_idx]
    point = polygon[i]
    next_point = polygon[next_idx]

    if is_convex(prev_point, point, next_point, direction):
        for j in range(len(polygon)):
            if j not in (prev_idx, i, next_idx) and is_point_inside_triangle(
                prev_point, point, next_point, polygon[j]
            ):
                return False
        return True
    return False


def is_convex(p, prev_p, next_p, direction):
    """
    Determine with the ccw, if 3 points are convex.
    """
    if direction == "counter-clockwise":
        cross_product = (next_p[0] - p[0]) * (prev_p[1] - p[1]) - (prev_p[0] - p[0]) * (
            next_p[1] - p[1]
        )
    else:
        cross_product = (prev_p[0] - p[0]) * (next_p[1] - p[1]) - (next_p[0] - p[0]) * (
            prev_p[1] - p[1]
        )
    return cross_product >= 0


def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def direction(points):
    """
    Determine whether the poligone points are given in a clockwise or counterclockwise direction.
    """
    point_0 = min(points, key=lambda p: (p[1], p[0]))
    idx_p0 = points.index(point_0)
    prev_idx = (idx_p0 - 1) % len(points)
    next_idx = (idx_p0 + 1) % len(points)

    prev_point = points[prev_idx]
    next_point = points[next_idx]
    while cross_product(point_0, next_point, prev_point) == 0:
        next_idx += 1
        next_point = points[next_idx]
    if cross_product(point_0, next_point, prev_point) > 0:
        return "clockwise"
    return "counter-clockwise"


def is_point_inside_triangle(p1, p2, p3, test_point):
    """
    Determine whether a point is in the triangle.
    """
    area_triangle = abs(
        0.5
        * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    )
    area1 = abs(
        0.5
        * (
            test_point[0] * (p2[1] - p3[1])
            + p2[0] * (p3[1] - test_point[1])
            + p3[0] * (test_point[1] - p2[1])
        )
    )
    area2 = abs(
        0.5
        * (
            p1[0] * (test_point[1] - p3[1])
            + test_point[0] * (p3[1] - p1[1])
            + p3[0] * (p1[1] - test_point[1])
        )
    )
    area3 = abs(
        0.5
        * (
            p1[0] * (p2[1] - test_point[1])
            + p2[0] * (test_point[1] - p1[1])
            + test_point[0] * (p1[1] - p2[1])
        )
    )

    return area_triangle == area1 + area2 + area3


def triangulate_polygon(coordinates):
    """
    Give the points of the triangulation of a polygon.
    """
    polygon = np.array(coordinates)
    triangles = []

    dir = direction(coordinates)
    while len(polygon) >= 3:
        ear_found = False
        for i in range(len(polygon)):
            if is_ear(polygon, i, dir):
                ear_found = True
                prev_idx = (i - 1) % len(polygon)
                next_idx = (i + 1) % len(polygon)
                triangles.append(
                    [
                        tuple(polygon[prev_idx]),
                        tuple(polygon[i]),
                        tuple(polygon[next_idx]),
                    ]
                )
                polygon = np.delete(polygon, i, axis=0)
                break

        if not ear_found:
            # No more ears can be clipped. The polygon may be self-intersecting.
            break

    return triangles


if __name__ == "__main__":
    coordinates = [(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)]
    triangles = triangulate_polygon(coordinates)
    for triangle in triangles:
        print(triangle)
