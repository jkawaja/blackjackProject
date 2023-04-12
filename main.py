import db
import random
import decimal

FILENAME = "money.txt"

# The type of suit
SUITS = ["♠", "♥", "♦", "♣"]
# The face value of the card
CARDS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

CARDS = [["Heart", "2", 2], ["Heart", "3", 3], ["Heart", "4", 4], ["Heart", "5", 5], ["Heart", "6", 6],
         ["Heart", "7", 7], ["Heart", "8", 8], ["Heart", "9", 9], ["Heart", "10", 10], ["Heart", "Jack", 10],
         ["Heart", "Queen", 10], ["Heart", "King", 10], ["Heart", "Ace", 11], ["Diamond", "2", 2], ["Diamond", "3", 3],
         ["Diamond", "4", 4], ["Diamond", "5", 5], ["Diamond", "6", 6], ["Diamond", "7", 7], ["Diamond", "8", 8],
         ["Diamond", "9", 9], ["Diamond", "10", 10], ["Diamond", "Jack", 10], ["Diamond", "Queen", 10],
         ["Diamond", "King", 10], ["Diamond", "Ace", 11], ["Spade", "2", 2], ["Spade", "3", 3], ["Spade", "4", 4],
         ["Spade", "5", 5], ["Spade", "6", 6], ["Spade", "7", 7], ["Spade", "8", 8], ["Spade", "9", 9],
         ["Spade", "10", 10], ["Spade", "Jack", 10], ["Spade", "Queen", 10], ["Spade", "King", 10],
         ["Spade", "Ace", 11], ["Club", "2", 2], ["Club", "3", 3], ["Club", "4", 4], ["Club", "5", 5], ["Club", "6", 6],
         ["Club", "7", 7], ["Club", "8", 8], ["Club", "9", 9], ["Club", "10", 10], ["Club", "Jack", 10],
         ["Club", "Queen", 10], ["Club", "King", 10], ["Club", "Ace", 11]]

def generateDeck(CARDS):
    deck = []
    for card in CARDS:
        deck.append(card)
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def getCardFaceValue(CARDS):
    pass



def getTotalValue(hand):
    total = 0
    for card in hand:
        total += card[2]
    return total



def showDealerHand(dealerHand):
    for i in range(len(dealerHand) - 1):
        print(f"{dealerHand[0][1]} of {dealerHand[0][0]}s")


def showHand(hand):
    for card in hand:
        print(f"{card[1]} of {card[0]}s")


def betCalculation(money):
    while True:
        try:
            bet = decimal.Decimal(input("Bet Amount: "))
            if bet >= 5 and bet <= 1000 and bet <= money:
                return bet
            else:
                print("Bet must be between $5 and $1000, and less than pot. Try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def dealPlayerCard(deck, hand):
    print(f"{deck[0][1]} of {deck[0][0]}s")
    if deck[0][1] == "Ace":
        checkTotal = getTotalValue(hand) + deck[0][2]
        if checkTotal > 21 and deck[0][1] == "Ace":
            deck[0][2] = 1
        elif checkTotal <= 21 and deck[0][1] == "Ace":
            aceChoice = input("You have drawn an Ace, would you like it to be 1 or 11? (enter 1 or 11): ")
            if aceChoice == "1":
                deck[0][2] = 1
            else:
                deck[0][2] = 11
    hand.append(deck[0])
    deck.pop(0)
    return hand

def dealDealerCard(deck, hand):
    if deck[0][1] == "Ace":
        checkTotal = getTotalValue(hand) + deck[0][2]
        if checkTotal > 21 and deck[0][1] == "Ace":
            deck[0][2] = 1
        else:
            deck[0][2] = 11
    hand.append(deck[0])
    deck.pop(0)
    return hand




# def main():
#     deck = [["Spade", "10", 10], ["Heart", "Ace", 11]]
#     # print(deck[0][2], deck[0][1])
#     playerHand = [] # , ["Diamond", "Ace", 11]
#     # showHand(playerHand)
#     # total = getTotalValue(playerHand)
#     # print("player hand", total)
#     # Draw an Ace
#     playerHand = dealPlayerCard(deck, playerHand)
#     playerHand = dealPlayerCard(deck, playerHand)
#     # showHand(playerHand)
#     # total = getTotalValue(playerHand)
#     # print("player hand", total)
#
#     # print(deck)
#
#
# if __name__ == '__main__':
#     main()

# Code starts here.
def main():
        print(f"BLACKJACK!\nBlackjack payout is 3:2")
        money = decimal.Decimal(db.readMoney())
        playGame = "y"

        while playGame.lower() == "y":
            #while loop trues
            playerTurn = True
            dealerTurn = True
            #Dealer / Player Hands
            dealerHand = []
            playerHand = []

            #Dealer / Player Points
            dealerPoints = 0
            playerPoints = 0
            print()
            print(f"Money: {money}: ")
            #Place your bet
            bet = betCalculation(money)
            print()

            #generate deck
            deck = generateDeck(CARDS)
            #shuffle deck
            deck = shuffleDeck(deck)

            #set up dealerHand
            dealerHand = dealDealerCard(deck, dealerHand)
            dealerHand = dealDealerCard(deck, dealerHand)
            print("DEALER'S SHOW CARD:")
            showDealerHand(dealerHand)
            print()
            #set up playerHand
            print(f"YOUR CARDS:")
            playerHand = dealPlayerCard(deck, playerHand)
            playerHand = dealPlayerCard(deck, playerHand)
            print()
            while playerTurn:
                playerChoice = input("Hit or stand? (hit/stand): ")
                print()
                if playerChoice.lower() == 'hit':
                    print(f"YOUR CARDS:")
                    showHand(playerHand)
                    playerHand = dealPlayerCard(deck, playerHand)
                    playerPoints = getTotalValue(playerHand)
                    dealerPoints = getTotalValue(dealerHand)
                    print()

                if playerPoints > 21:
                    print()
                    print(f"YOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}")
                    print("You busted. Sorry, you lose.")
                    money -= bet
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    print()
                    dealerTurn = False
                    playerTurn = False

                elif playerChoice.lower() == "stand":
                    playerTurn = False

            # Dealer's Turn
            while dealerTurn:
                print(f"DEALER'S CARDS:")
                showHand(dealerHand)
                print()
                dealerPoints = getTotalValue(dealerHand)
                if getTotalValue(dealerHand) > getTotalValue(playerHand):
                    print(f"YOUR POINTS: {getTotalValue(playerHand)}")
                    print(f"DEALER'S POINTS: {getTotalValue(dealerHand)}")
                    print()
                    print(f"Sorry. You lose.")
                    money -= bet
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    dealerTurn = False
                elif getTotalValue(dealerHand) >= 17 and getTotalValue(dealerHand) < getTotalValue(playerHand):
                    print()
                    print(f"YOUR POINTS: {getTotalValue(playerHand)}")
                    print(f"DEALER'S POINTS: {getTotalValue(dealerHand)}")
                    print()
                    print("Dealer stays. You win!")
                    money += bet
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    dealerTurn = False
                elif getTotalValue(dealerHand) < 17:
                    dealerHand = dealDealerCard(deck, dealerHand)
                    if getTotalValue(dealerHand) > 21:
                        print()
                        print(f"YOUR POINTS: {getTotalValue(playerHand)}")
                        print(f"DEALER'S POINTS: {getTotalValue(dealerHand)}")
                        print()
                        print("Dealer busted. You win.")
                        money += bet
                        db.writeMoney(money)
                        print(f"Money: {money}")
                        dealerTurn = False
                elif getTotalValue(dealerHand) == getTotalValue(playerHand):
                    print()
                    print(f"YOUR POINTS: {getTotalValue(playerHand)}")
                    print(f"DEALER'S POINTS: {getTotalValue(dealerHand)}")
                    print()
                    print("Dealer stays. It's a tie. Player gets money back.")
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    dealerTurn = False


            playGame = input("Play again? (y/n): ")
            print()
        print(f"Come back soon!\nBye!")


if __name__ == '__main__':
    main()

    #JUNK CODE DOWN HERE FOR TESTING
    #
    # deck_card_one = deck[0]
    #
    # playerHand = []

    # print("playerHand", playerHand)
    # handValue = getTotalValue(playerHand)
    # print("handValue", handValue)

    # print("deck first card popped", deck)
    #
    # testHand = [['Diamond', '5', 5], ['Club', 'Queen', 10]]
    #
    #
    # showDealerHand(testHand)
    #
    # print()
    # print()
    # print()
    #
    # showHand(testHand)


       #Show dealer's hand


    # #test subtract money
    # print("Test Subtract Money")
    # bet = betCalculation()
    # money = money - bet
    # db.writeMoney(money)
    # print(money)
    #
    # #add money test
    # print("Test Add Money")
    # bet = betCalculation()
    # money = money + bet
    # db.writeMoney(money)
    # print(money)

    #generate deck test


