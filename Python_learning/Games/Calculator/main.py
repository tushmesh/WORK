# from replit import clear
# from art import logo
# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def sub(n1, n2):
    return n1 - n2


# Division
def div(n1, n2):
    return n1 / n2


# Multiply
def mul(n1, n2):
    return n1 * n2


operation = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul
}


def calculator():
    ask = True
    # print(logo)
    num1 = float(input("Enter the first number : "))

    while ask == True:

        for symbols in operation:
            print(symbols)

        opr_symbol = input("Pick an operation to calculate: ")
        num2 = float(input("Enter the next number : "))
        calculate = operation[opr_symbol]
        first_answer = calculate(num1, num2)
        print(f"{num1} {opr_symbol} {num2} = {first_answer}")

        conti_nue = input("Do you want to continue with next calculation y / n or type exit to stop : ")
        if conti_nue == 'n':
            ask = False
            calculator()
        elif conti_nue == "exit":
            ask = False
        else:
            num1 = first_answer


calculator()
# opr_symbol = input("Pick an operation to calculate: ")
# num3 = int(input("Enter the next number : "))
# calculate = operation[opr_symbol]
# second_answer = calculate(first_answer , num3)
# print(f"{first_answer} {opr_symbol} {num3} = {second_answer}")
# conti_nue = input("Do you want to continue with new calculation y / n : ")
# if conti_nue == 'n':
# 	ask = False
# else:
# 	clear()
