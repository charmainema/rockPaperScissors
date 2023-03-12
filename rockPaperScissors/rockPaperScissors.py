# import modules
import random
import time
import pygame

# store possible moves
moves = ["rock", "paper", "scissors", "lizard", "spock"]

# store possible win/loss combinations for default mode (wins assigned 1, losses assigned 0)
winLose = {
    "rock": {
        "rock": ["It's a draw!"],
        "paper": ["You lose!", "The paper covers your rock.", 0],
        "scissors": ["You win!", "Your rock crushes the scissors.", 1],
        "lizard": ["You win!", "Your rock smashes the lizard.", 1],
        "spock": ["You lose!", "Spock vaporizes your rock.", 0]
    },
    "paper": {
        "rock": ["You win!", "Your paper covers the rock.", 1],
        "paper": ["It's a draw!"],
        "scissors": ["You lose!", "The scissors cut your paper.", 0],
        "lizard": ["You lose!", "The lizard eats your paper.", 0],
        "spock": ["You win!", "Your paper disproves Spock.", 1]
    },
    "scissors": {
        "rock": ["You lose!", "The rock smashes your scissors.", 0],
        "paper": ["You win!", "Your scissors cut the paper.", 1],
        "scissors": ["It's a draw!"],
        "lizard": ["You win!", "Your scissors cut the lizard.", 1],
        "spock": ["You lose!", "Spock smashes your scissors.", 0]
    },
    "lizard": {
        "rock": ["You lose!", "The rock smashes your lizard.", 0],
        "paper": ["You win!", "Your lizard eats the paper.", 1],
        "scissors": ["You lose!","The scissors cut your lizard.", 0],
        "lizard": ["It's a draw!"],
        "spock": ["You win!", "Your lizard poisons Spock.", 1]
    },
    "spock": {
        "rock": ["You win!", "Spock vaporizes the rock.", 1],
        "paper": ["You lose!", "The paper disproves Spock.", 0],
        "scissors": ["You win!", "Spock smashes the scissors.", 1],
        "lizard": ["You lose!", "The lizard poisons spock.", 0],
        "spock": ["It's a draw!"]
    }
}

# store possible win/loss combinations for ultimate game mode
ultWinLose = {
    "rock": {
        "rock": ["It's a draw!"],
        "paper": ["You lose!", 0],
        "scissors": ["You win!", 1],
        "lizard": ["You win!", 1],
        "spock": ["You lose!", 0]
    },
    "paper": {
        "rock": ["You win!", 1],
        "paper": ["It's a draw!"],
        "scissors": ["You lose!", 0],
        "lizard": ["You lose!", 0],
        "spock": ["You win!", 1]
    },
    "scissors": {
        "rock": ["You lose!", 0],
        "paper": ["You win!", 1],
        "scissors": ["It's a draw!"],
        "lizard": ["You win!", 1],
        "spock": ["You lose!", 0]
    }, 
    "nothing": {
        "rock": ["You lose!", 0],
        "paper": ["You lose!", 0],
        "scissors": ["You lose!", 0],
        "lizard": ["You lose!", 0],
        "spock": ["You lose!", 0]
    }
}

# initialize variables
winCount = 0
wins = []
lossCount = 0
losses = []
totalTime = 0.0

# default game
def game():
    global totalTime
    global winCount
    global lossCount
    global wins
    global losses
    randomMove = random.choice(moves)
    userMove = input("Select \"rock\", \"paper\", \"scissors\", \"lizard\" or \"spock\", or \"q\" to exit to game selection: ")
    # store initial time
    initialTime = round(time.time(), 2)
    while userMove != "q":
        if userMove != "rock" and userMove != "paper" and userMove != "scissors" and userMove != "lizard" and userMove != "spock":
            print("Not a valid selection. Please re-enter selection.")
            userMove = input("Select \"rock\", \"paper\", \"scissors\", \"lizard\" or \"spock\", or \"q\" to exit to game selection: ")
            continue
        print("~~~~~~~~~~~~~")
        for i in moves:
            print("*%s*!" % i)
            time.sleep(0.5)
        print("~~~~~~~~~~~~~")
        print("Computer's choice: %s" % randomMove)
        print("Your choice: %s" % userMove)
        # print extra message if not a draw
        if len(winLose[userMove][randomMove]) >= 2:
            print("%s" % (winLose[userMove][randomMove][1]))
        # print win/loss combination
        print("%s" % (winLose[userMove][randomMove][0]))
        print("~~~~~~~~~~~~~")
        # add 1 to winCount if win/loss combination is assigned a win
        if len(winLose[userMove][randomMove]) >= 3:
            if winLose[userMove][randomMove][2] == 1:
                winCount += 1
                wins.append(1)
            else:
                lossCount += 1
                losses.append(0)
        userMove = input("Select \"rock\", \"paper\", \"scissors\", \"lizard\" or \"spock\", or \"q\" to exit to game selection: ")
        randomMove = random.choice(moves)
    #store final time and calculate total time
    finalTime = round(time.time(), 2)
    timeCalc = round(finalTime - initialTime, 2)
    totalTime += timeCalc
    time.sleep(1)
    print("")
    print("~~~~~~~~~~~~~")
    print("Your wins: %s" % winCount)
    print("Your losses: %s" % lossCount)
    print("Your play time: %s seconds" % timeCalc)
    if winCount > lossCount:
        print("**Wow, you're good at this game!**")
    elif lossCount > winCount:
        print("**Oh... you aren't so good at this game are you...**")
    elif lossCount == 0 and winCount == 0:
        print("**You didn't win anything but you didn't lose anything, I guess.**")
    else:
        print("**Well, I mean you aren't good but you aren't bad.**")
    print("")
    winCount = 0
    lossCount = 0

# ultimate game mode
def ultGame():
    # globalize variables
    global winCount
    global lossCount
    global totalTime

    # start timer
    initialTime = round(time.time(), 2)

    # assign health values
    totalHealth = 100
    userHealth = 100
    computerHealth = 100
    print("~~~~~~~~~~~~~")
    print("You are now venturing into the abyss...")
    time.sleep(1)
    for i in range(10):
        print(".")
        time.sleep(0.4)
    print("This is no ordinary \"rock, paper, scissors\" game! This is *ULTIMATE* rock, paper, scissors! There is no \"lizard\" or \"spock\" move in this game, so please don't try those moves. You will lose if you try. I'm not kidding, try it if you don't believe me. Also type the move in properly or you will lose.")
    print("")
    print(input("(Press enter to continue)"))
    print("When you are ready, open the pygame window. (It should appear below in your computer taskbar)")
    print("Begin by typing in either of \"rock\", \"paper\", or \"scissors\". Press enter to enter the move, and watch what happens! Close the pygame window when the game is complete.")
    # pygame script                                                                               
    pygame.init()
    # initialize game
    window = pygame.display.set_mode((963, 685))
    # draw background
    window.blit(pygame.image.load("background.jpg"), (0,0))
    # draw hand default positions
    window.blit(pygame.image.load("a1.png"), (0,0))
    window.blit(pygame.image.load("anim 1.png"), (0,0))
    pygame.display.update()
    pygame.display.set_caption("Ultimate Rock Paper Scissors")
    clock = pygame.time.Clock()
    game = True

    # animations
    leftHandAnim = [pygame.image.load("anim 1.png"), pygame.image.load("anim 2.png"), pygame.image.load("anim 3.png"), pygame.image.load("anim 4.png"), pygame.image.load("anim 5.png"), pygame.image.load("anim 6.png"), pygame.image.load("anim 7.png"), pygame.image.load("anim 8.png"), pygame.image.load("anim 9.png"), pygame.image.load("anim 10.png"), pygame.image.load("anim 11.png"), pygame.image.load("anim 12.png")]

    rightHandAnim = [pygame.image.load("a1.png"), pygame.image.load("a2.png"), pygame.image.load("a3.png"), pygame.image.load("a4.png"), pygame.image.load("a5.png"), pygame.image.load("a6.png"), pygame.image.load("a7.png"), pygame.image.load("a8.png"), pygame.image.load("a9.png"), pygame.image.load("a10.png"), pygame.image.load("a11.png"), pygame.image.load("a12.png"),]

    # rock/paper/scissors moves
    rockLeft = pygame.image.load("rock left.png")
    rockRight = pygame.image.load("rock right.png")
    paperleft = pygame.image.load("paper left.png")
    paperRight = pygame.image.load("paper right.png")
    scissorsLeft = pygame.image.load("scissors left.png")
    scissorsRight = pygame.image.load("scissors right.png")

    # create input box
    defaultText = "Enter \"rock\", \"paper\", or \"scissors\" to beat the enemy!"
    userMove = ""

    # create health bars
    userHealthDisplay = pygame.Rect(30, 40, 400, 30)
    userHealthBar = pygame.Rect(30, 40, 400, 30)
    computerHealthDisplay = pygame.Rect(530, 40, 400, 30)
    computerHealthBar = pygame.Rect(530, 40, 400, 30)

    # text properties
    font = pygame.font.Font(None, 32)
    mainFont = pygame.font.Font(None, 70)
    textColor = (255, 255, 255)
    redText = (255, 0, 0)
    greenText = (38, 191, 0)
    whiteColor = (217, 217, 217)

    # run game
    while game == True:
        # check for user action
        for userAction in pygame.event.get():
            # quit game is window is closed
            if userAction.type == pygame.QUIT:
                game = False
            # use inputBox
            if userAction.type == pygame.KEYDOWN:
                if userAction.key == pygame.K_RETURN:
                    for i in range(12):
                        window.blit(pygame.image.load("background.jpg"), (0, 0))
                        # draw health displays
                        pygame.draw.rect(window, whiteColor, userHealthBar, 0)
                        pygame.draw.rect(window, greenText, userHealthDisplay, 0)
                        pygame.draw.rect(window, whiteColor, computerHealthBar, 0)
                        pygame.draw.rect(window, redText, computerHealthDisplay, 0)
                        # draw rock-paper-scissors animation
                        window.blit(leftHandAnim[i], (0, 0))
                        window.blit(rightHandAnim[i], (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(45)
                    # assign computer move
                    randomMove = random.choice(moves[:3])
                    if userMove != "rock" and userMove != "paper" and userMove != "scissors":
                        userMove = "nothing"
                    # draw background over
                    window.blit(pygame.image.load("background.jpg"), (0,0))
                    # health calculations
                    if len(ultWinLose[userMove][randomMove]) >= 2:
                        # if win/loss combination is assigned a loss:
                        if ultWinLose[userMove][randomMove][1] == 0:
                            # subtract 10 from userHealth
                            userHealth -= 10
                            # update x position for userHealthDisplay based on health %
                            healthX = 400 * userHealth / totalHealth
                            # draw background
                            window.blit(pygame.image.load("background.jpg"), (0,0))
                            # draw userHealthDisplay + userHealthBar
                            userHealthDisplay = pygame.Rect(30, 40, healthX, 30)
                            pygame.draw.rect(window, greenText, userHealthDisplay, 0)
                            pygame.draw.rect(window, whiteColor, userHealthBar, 0)
                        # if win/loss combination is assigned a win:
                        elif ultWinLose[userMove][randomMove][1] == 1:
                            # subtract 20 from computerHealth
                            computerHealth -= 20
                            # update x position for computerHealthDisplay based on health %
                            healthX = 400 * computerHealth / totalHealth
                            window.blit(pygame.image.load("background.jpg"), (0,0))
                            computerHealthDisplay = pygame.Rect(530, 40, healthX, 30)
                            # draw computerHealthDisplay + computerHealthBar
                            pygame.draw.rect(window, redText, computerHealthDisplay, 0)
                            pygame.draw.rect(window, whiteColor, computerHealthBar, 0)
                    # check user move and assign image
                    if userMove == "rock":
                        window.blit(rockLeft, (0, 0))
                    elif userMove == "paper":
                        window.blit(paperleft, (0, 0))
                    elif userMove == "scissors":
                        window.blit(scissorsLeft, (0, 0))
                    else:
                        userMove = "nothing"
                        # draw hand default position
                        window.blit(pygame.image.load("anim 1.png"), (0,0))
                    # check computer move and assign image
                    if randomMove == "rock":
                        window.blit(rockRight, (0, 0))
                    elif randomMove == "paper":
                        window.blit(paperRight, (0, 0))
                    elif randomMove == "scissors":
                        window.blit(scissorsRight, (0, 0))
                    # display moves + render text
                    userString = "You used %s!" % userMove
                    computerString = "The enemy used %s!" % randomMove
                    window.blit(mainFont.render(userString, True, greenText), (130, 130))
                    window.blit(mainFont.render(computerString, True, redText), (130, 200))
                    userMove = ""
                    # update window
                    pygame.display.flip()
                elif userAction.key == pygame.K_BACKSPACE:
                    userMove = userMove[:-1]
                    # draw background
                    window.blit(pygame.image.load("background.jpg"), (0,0))
                    # draw hand default positions
                    window.blit(pygame.image.load("anim 1.png"), (0,0))
                    window.blit(pygame.image.load("a1.png"), (0,0))
                else:
                    userMove += userAction.unicode

        # draw health displays
        pygame.draw.rect(window, whiteColor, userHealthBar, 0)
        pygame.draw.rect(window, greenText, userHealthDisplay, 0)
        pygame.draw.rect(window, whiteColor, computerHealthBar, 0)
        pygame.draw.rect(window, redText, computerHealthDisplay, 0)
        # Render the current text.
        txt = font.render(userMove, True, textColor)
        # Blit the text.
        window.blit(txt, (620, 600))
        # Blit the input_box rect.
        window.blit(font.render(defaultText, True, textColor), (30, 600))
        pygame.display.flip()

        # check if user wins or loses:
        if computerHealth == 0:
            # display win message
            window.blit(pygame.image.load("background.jpg"), (0, 0))
            window.blit(mainFont.render("You win!", True, greenText), (390, 300))
        elif userHealth == 0:
            # display loss message
            window.blit(pygame.image.load("background.jpg"), (0, 0))
            window.blit(mainFont.render("You lose!", True, redText), (390, 300))
        clock.tick(60)

    pygame.quit()

    # stop timer and calculate total time
    finalTime = round(time.time(), 2)
    timeCalc = round(finalTime - initialTime, 2)
    totalTime += timeCalc

    time.sleep(1)

    # check whether user won and display according message and assign wins/losses
    if computerHealth == 0:
        # add 1000 to wins
        for i in range(1000):
            wins.append(1)
        winCount = 1000
        lossCount = 0
        message = "**WOWWWWWWWWWWWW YOU WON!!! :)**"
    elif userHealth == 0:
        # add 100 to losses
        for i in range(1000):
            losses.append(1)
        winCount = 0
        lossCount = 1000
        message = "**How did you even lose? The game was rigged to remove 20 health from the enemy and 10 health from you....**"
    else:
        message = "**Oh wow, you didn't even try to beat the game! >:(**"
    # final message display to console
    print("")
    print("~~~~~~~~~~~~~")
    print("Your wins: %s" % winCount)
    print("Your losses: %s" % lossCount)
    print("Your play time: %s seconds" % timeCalc)
    print("%s" % message)
    

# initialize game
print("")
choice = input("Would you like to play the \"Rock, Paper, Scissors, Lizard, Spock\" game? (Type \"play\" to play the default game. Type \"ult\" to play the ultimate game mode. Type \"stats\" to view your overall stats. Type \"q\" to quit.): ")
if choice != "play" and choice != "ult" and choice != "stats" and choice != "q":
        print("~~~~~~~~~~~~~")
        print("Not a valid selection. Please re-enter selection.")
        choice = input("Would you like to play the \"Rock, Paper, Scissors, Lizard, Spock\" game? (Type \"play\" to play the default game. Type \"ult\" to play the ultimate game mode. Type \"stats\" to view your overall game stats. Type \"q\" to quit.): ")

# play game
while choice != "q":
    if choice == "play":
        game()
    elif choice == "ult":
        ultGame()
    elif choice == "stats":
        time.sleep(0.75)
        print("----------------")
        print("Your total wins: %s" % len(wins))
        print("Your total losses: %s" % len(losses))
        print("Your total play time: %s seconds" % round(totalTime, 2))
        if len(wins) > len(losses):
            print("**Wow, you're good at this game!**")
        elif len(losses) > len(wins):
            print("**Oh... you aren't so good at this game are you...**")
        elif len(losses) == 0 and len(wins) == 0:
            print("**You didn't win anything but you didn't lose anything, I guess.**")
        else:
            print("**Well, I mean you aren't good but you aren't bad.**")
        print("----------------")
    elif choice == "q":
        continue
    else:
        print("~~~~~~~~~~~~~")
        print("Not a valid selection. Please re-enter selection.")
        choice = input("Game selection: (Type \"play\" to play the default game. Type \"ult\" to play the ultimate game mode. Type \"stats\" to view your overall game stats. Type \"q\" to quit.): ")
        continue
    print("")
    choice = input("Game selection: (Type \"play\" to play the default game. Type \"ult\" to play the ultimate game mode. Type \"stats\" to view your overall game stats. Type \"q\" to quit.): ")

print("")
print("~~~~~~~~~~~~~")
print("Your total wins: %s" % len(wins))
print("Your total losses: %s" % len(losses))
if len(wins) > len(losses):
    print("**Wow, you're good at this game!**")
elif len(losses) > len(wins):
    print("**Oh... you aren't so good at this game are you...**")
elif len(losses) == 0 and len(wins) == 0:
    print("**You didn't win anything but you didn't lose anything, I guess.**")
else:
    print("**Well, I mean you aren't good but you aren't bad.**")
print("")
