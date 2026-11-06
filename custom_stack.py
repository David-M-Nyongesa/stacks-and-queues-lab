def is_valid_parentheses(s: str) -> bool:

    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())

    stack = [] 

    for char in s:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    for example in ["()", "{[()]}", "([]{})", "(", "([)]", "(()"]:
        print(f"{example!r:10} -> {is_valid_parentheses(example)}")
