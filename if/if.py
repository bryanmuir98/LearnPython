is_male = False
is_tall = True

if is_male and is_tall:
    print("You're a tall male")
elif not(is_male) and not(is_tall):
    print("You're not a male and you're not tall")
elif is_male and not(is_tall):
    print("You're a male but you're not tall")
else:
    print("You're not a male but you're tall")
