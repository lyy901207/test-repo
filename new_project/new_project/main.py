def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test case
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 8
    result = binary_search(arr, target)
    print(
        f"Target {target} found at index {result}"
        if result != -1
        else "Target not found"
    )
