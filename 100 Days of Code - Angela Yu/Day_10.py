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

num1 = int(intput("what's the first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number"))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

    