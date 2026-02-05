# Problem: Find sum of first N natural numbers using recursion
# Time Complexity: O(n)
# Space Complexity: O(n)

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = 5
print("Sum of first", n, "numbers is", sum_n(n))
