infix = list(input())
out = []
stack = []
ops = {
    '-' : 0,
    '+' : 1,
    '/' : 2,
    '*' : 3
}

for token in infix:
    if token in ops.keys():
        while len(stack) != 0 and stack[-1] != '(' and ops[token] < ops[stack[-1]] :
            out.append(stack.pop())
        stack.append(token)

    elif token == '(':
        stack.append(token)

    elif token == ')':
        while stack[-1] != '(':
            out.append(stack.pop())
        stack.pop()

    else:
        out.append(token)

while len(stack) != 0:
    out.append((stack.pop()))
print(*out)

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0
def to_prefix(expression):
    stack = []
    output = []
    operators = ['+', '-', '*', '/', '^']

    for char in reversed(expression):
        if char.isalnum():
            output.append(char)

        elif char == ')':
            stack.append(char)

        elif char == '(':
            while stack and stack[-1] != ')':
                output.append(stack.pop())
            stack.pop()

        elif char in operators:
            while stack and precedence(char) < precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(reversed(output))


# Пример использования
infix = infix
prefix = to_prefix(infix)
print(prefix)
