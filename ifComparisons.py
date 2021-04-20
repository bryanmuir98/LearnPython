def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num3:
        greatest = num2
    else:
        greatest = num3
    return greatest

print((max_num(12,56,55)))

