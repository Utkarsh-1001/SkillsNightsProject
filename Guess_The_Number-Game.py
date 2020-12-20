hid = 46
chance = 6
print("....HANGMAN....")
print("A two digit no. is hidden in here....")
print("\t;;;;You have 6 chances to guess it;;;;")
while(chance>0):
    print("Enter a number:")
    game = int(input())
    if(game<hid):
        print("You need to higher your stakes")
        chance= chance - 1
        print("Remaining chances are:", chance)
        if(chance<1):
            print("Sorry, you lost your chances.")
    elif(game>hid):
        print("Oh! You need to calm down a bit")
        chance = chance -1
        print("Remaining chances are:", chance)
        if(chance<1):
            print("Sorry, no chances left.")
            print("--GAME OVER--")
    else:
        print("Wow! You got it.")
        print('You got it with ',chance-1,' chances remaining...')
        break
