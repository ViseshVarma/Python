# calculator

# add
def add(n1, n2):
    return n1 + n2

# sub
def sub(n1, n2):
    return n1 - n2

# multiply
def mul(n1, n2):
    return n1 * n2

#div
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1 = int(intput("what's the first number"))
num2 = int(input("What's the second number"))