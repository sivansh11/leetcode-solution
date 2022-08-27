def maxArea(height):
    def area(index1, index2, height):
        h = min(height[index1], height[index2])
        w = abs(index1 - index2)
        return h * w
    l = 0
    r = len(height) - 1
    best_area = 0
    while r != l:
        val = area(l, r, height)
        if val > best_area:
            best_area = val
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return best_area


print(maxArea([1,8,6,2,5,4,8,3,7]))
