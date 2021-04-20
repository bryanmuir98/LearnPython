secretWord = "monkey"
guess = ""
x = 10

while guess != secretWord:
    guess = input("Enter your guess for the secret word (zoo animals) (" + str(x) + " guesses remaining): ")
    x -= 1
    if x == 0:
        print("Sorry! Better luck next time...")
        break
    elif guess == secretWord:
        print("You guessed it! The secret word was: " + secretWord.upper())
        break
