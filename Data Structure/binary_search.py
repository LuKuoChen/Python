def binary_search(list: list[int], target: int) -> int:
    list.sort()
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1))
print(binary_search([10, 5, 8, 1, 7, 100, 50, 999, -1, -7, -56], -1))
print(binary_search([10, 5, 8, 1, 7, 100, 50, 999, -1, -7, -56], -56))
