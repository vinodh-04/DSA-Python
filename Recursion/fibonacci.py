# Problem: Generate Fibonacci number using recursion
# Time Complexity: O(2^n) (basic recursive approach)
# Space Complexity: O(n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
print("Fibonacci number at position", n, "is", fibonacci(n))
