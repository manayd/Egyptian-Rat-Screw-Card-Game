import random

deck = []
specialCards = ['Ace', 'King', 'Queen', 'Jack']
for x in specialCards:
   for i in range(4):
    deck.append(x)
for i in range(2,11):
    for j in range(4):
        deck.append(str(i))

random.shuffle(deck)

playerOneDeck = deck[:26]
playerTwoDeck = deck[26:]
currentPile = []
playerOneScore = 0
playerTwoScore = 0
score = 0
playerOneTurn = False
while(len(playerOneDeck) > 0 & len(playerTwoDeck)):
    playerOneTurn = not playerOneTurn
    topCard = "0"
    if playerOneTurn:
        topCard = playerOneDeck[0]
        playerOneDeck.pop(0)
    else:
        topCard = playerTwoDeck[0]
        playerTwoDeck.pop(0)
    print(topCard)
    currentPile.insert(0, topCard)

    userVal=""
    if(len(currentPile) > 2):
        userVal = input("Slap?:")
        if userVal == 'y':
            roundScore = checkSlap(currentPile)
            playerOneScore += roundScore
            if(roundScore > 0):
                print('------\n')
                print("Player One Score " + str(playerOneScore))
                print('------\n')
        else:
            roundScore = checkSlap(currentPile)
            playerTwoScore += roundScore
            if roundScore > 0:
                print('------\n')
                print("Player Two Score " + str(playerTwoScore))
                print('------\n')
        

print("Final Scores:\nFirst Player's Score " + str(playerOneScore) + "\nSecond Player's Score " + str(playerTwoScore))
winner = ""
if playerOneScore > playerTwoScore:
    winner = "Player One Wins!"
elif playerOneScore < playerTwoScore:
    winner = "Player Two Wins!"
else:
    winner = "It's a Tie!"

print(winner)

def checkSlap(pile):
    score=0
    if (((pile[1] == 'King') & (pile[0] == 'Queen')) | ((pile[1] == 'Queen') & (pile[0] in 'King'))):
            score+= len(pile)

    elif (pile[0] == pile[1]):
            score+= len(pile)

    elif (pile[0] == pile[2]):
            score+= len(pile)

    elif (pile[len(pile) - 1] == pile[0]):
            score+= len(pile)

    elif ((pile[0] + pile[1] == 10) | ((pile[0] + pile[2] == 10) & (pile[1] in specialCards == True))):
            score+= len(pile)

    return score