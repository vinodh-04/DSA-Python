# Check if parentheses are balanced using stack

def is_balanced(expr):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()

    return len(stack) == 0

expr = "{[()()]}"
print("Balanced:", is_balanced(expr))
