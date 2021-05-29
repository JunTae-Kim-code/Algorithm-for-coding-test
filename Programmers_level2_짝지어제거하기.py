def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        while True:
            if len(stack)<2 or stack[-1] != stack[-2]:
                break
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if stack:
        return 0
    else:
        return 1