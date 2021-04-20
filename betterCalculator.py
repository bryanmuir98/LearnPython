num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number: "))
def betterCalc(num1,op,num2):
    answer = 0
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2
    elif op == "/":
        answer = num1 / num2
    else:
        print("Please enter valid operator!")
    return answer
print("Your answer is: " + str(betterCalc(num1,op,num2)))
