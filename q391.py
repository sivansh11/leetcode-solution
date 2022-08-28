def is_over_lapping(rectangle1: list[int], rectangle2: list[int]) -> bool:
    x1,y1,a1,b1 = rectangle1
    x2,y2,a2,b2 = rectangle2

    if a1 > x2 and x1 < a2 and \
       b1 > y2 and y1 < b2:
        return True
    return False


def rectangle_union(rectangle1: list[int], rectangle2: list[int]):
    x1,y1,a1,b1 = rectangle1
    x2,y2,a2,b2 = rectangle2
    return [min(x1, x2), min(y1, y2), max(a1, a2), max(b1, b2)]


def area(rectangle: list[int]) -> int:
    x,y,a,b = rectangle
    return (a - x) * (b - y)


def is_perfect_touching(rectangle1: list[int], rectangle2: list[int]) -> bool:
    x1,y1,a1,b1 = rectangle1
    x2,y2,a2,b2 = rectangle2

    if a1 == x2 or x1 == a2 or \
       b1 == y2 or y1 == b2:
        return True
    return False


def isRectangleCover(rectangles: list[list[int]]) -> bool:
    if len(rectangles) in (0, 1):
        return True
    total_area = area(rectangles[0])
    total_rectangle = rectangles[0]
        

    for i in range(len(rectangles) - 1):
        for j in range(i + 1, len(rectangles)):    
            if is_over_lapping(rectangles[i], rectangles[j]):
                return False
        total_rectangle = rectangle_union(total_rectangle, rectangles[i])
        total_area += area(rectangles[i])

    total_rectangle = rectangle_union(total_rectangle, rectangles[-1])
    total_area += area(rectangles[-1])

    total_rectangle_area = area(total_rectangle)
    if total_area != total_rectangle_area:
        return False
    return True
    
assert isRectangleCover([[0,0,1,1],[0,1,3,2],[1,0,2,2]]) is False
