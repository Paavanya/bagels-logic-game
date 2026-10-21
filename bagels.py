#Bagels
import random
answer = random.randint(100,999)
print("I am thinking of a 3-digit number. Try to guess what it is." , "Clues:", sep = "\n")
print("Pico - A digit is correct but in the wrong position.")
print("Fermi - A digit is correct but in the right position.")
print("Bagels - No digit is correct.")
print("I have thought of a 3-digit number. You have 10 guesses to get it.")

guessed = 0
n = 10

while n > 0:
    try:
        num = int(input("Please enter your guess: "))
        if num < 100 or num > 999:
            print("Please enter a 3-digit number only.")
            continue
        
    except ValueError:
        print("Please enter a 3-digit whole number.")
        
    else:
        
        if num == answer:
            print("You got it!")
            break

        else:
            lsanswer = list(str(answer))
            lsnum = list(str(num))
            
            for i in range(0, 3):
                if lsnum[i] == lsanswer[i]:
                    lsanswer[i] = "removed1"
                    lsnum[i] = "removed2"
                    print("Fermi" , end = " ")
                    guessed = 1

            for i in range(0,3):
                for j in range(0 , 3):
                    if lsanswer[i] == lsnum[j]:
                        lsanswer[i] = "removed1"
                        lsnum[j] = "removed2"
                        print("Pico", end = " ")
                        guessed = 1

            if guessed != 1:
                print("Bagels", end = "")

            n = n - 1
            print("")
            guessed = 0

if n == 0:

    print("You lost. Answer was:" , answer)
