import random
RPS = ['rock', 'paper', 'scissors']
def points():
    value = int(input("Enter for how many points you want to play this game: "))
    return value
def user():
    choice = input("Enter your choice rock, paper, scissors: ").lower()
    while choice not in RPS:
        print("You chosed an invalid option")
        choice = input("Enter you choice in rock or paper or scissors: ").lower()
    
    return choice

def computer():
    choice = random.choice(RPS)
    return choice

def play():
    Up = 0
    Cp = 0
    P = points()
    while Up!=P and Cp != P:
        U = user()
        C = computer()
        print('Computer choosen: ', C)
        if (
        (U == 'rock' and C == 'scissors') or
        (U == 'paper' and C == 'rock') or
        (U == 'scissors' and C == 'paper')
        ):
            Up += 1
            print('You got a point')
        elif (U==C):
            print('No one gets a point')
        else:
            Cp += 1
            print('Computer got a point')
    if Up == P:
        print('You Win!..')
    else:
        print('Computer Win')


if __name__ == "__main__":
    play()