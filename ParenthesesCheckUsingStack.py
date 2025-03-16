from Stack import *

def parenthesis_check(par_pattern):
    stack = Stack()
    for i in par_pattern:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                return False
    return True


# par_pattern = "((()))()"
# par_pattern = "((()))())"
par_pattern = ")()"
res = parenthesis_check(par_pattern)
if res:
    print("Pattern looks valid")
else:
    print("Pattern is NOT valid")

