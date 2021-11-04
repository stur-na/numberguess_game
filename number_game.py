import random
#this program taught me more about looping and catching errors,


#error check to make sure a number is entered by the player
def checkerror():
    while True:
        try:
            userinput = int(input('Guess a number: '))
        except ValueError:
            print('please enter a number instead ')
            continue
        break
    
#logic to compare the guessed number and the player number
def compare(i, c):
    if i == c:
        print('Hurray! You guessed the number correctly')
        
    else:
        print('Aw! that is the wrong answer, '+ 'you have {} trial left'.format(5-game))

#display to the player the guessed number
def checknum():
    print('The number was {} '.format(computer))

#start game
print('Welcome to the guess game, pick a number between 1 and 50..you have 5 guesses per game')
game = 1
while game < 6:
    computer = random.randint(0,50)
    compare(checkerror(), computer)
    checknum()
    game+=1
    if game == 6:
        print('bye bye!')
