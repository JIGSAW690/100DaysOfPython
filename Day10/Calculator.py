from art import logo

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

operators = ['+','-','*','/']

def calculator():
    print(logo)
    a = int(input("What's the first number?\n"))
    calculation_on = True
    while calculation_on:
        for i in operators:
            print(i)
        choice = input('Pick an Operation\t')
        b = int(input("What's the next number\t"))
        calculator_dic = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b), '/': div(a, b)}
        print(f"{a} {choice} {b} = {calculator_dic[choice]}")
        choice_one = input(f"Type 'y' to continue calculating with {calculator_dic[choice]}, or type 'new' to start a new calculation, or 'exit' to exit the application").lower()
        if (choice_one == 'y'):
            a = calculator_dic[choice]
        elif (choice_one == 'new'):
            calculation_on = False
            print('\n'*5)
            calculator()
        else:
            return

calculator()






