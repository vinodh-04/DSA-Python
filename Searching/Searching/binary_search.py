# Problem: Binary Search
# Approach: Divide and conquer
# Time Complexity: O(log n)
# Space Complexity: O(1)

arr = [10, 20, 30, 40, 50]
key = 40

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
