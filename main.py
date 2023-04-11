import db
import random

FILENAME = "money.txt"

# The type of suit
SUITS = ["♠", "♥", "♦", "♣"]
# The face value of the card
CARDS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

dealerHand = []

playerHand = []

def generateDeck():
    deck = []
    for suit in SUITS:
        for card in CARDS:
            deck.append((card, suit))
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def getCardFaceValue(CARDS):
    for card in CARDS:
        if card == "J":
            card = 10

HAND = [('J', '♣'), ('Q', '♠')]

def getTotalValue(HAND):
    total = 0
    for card in HAND:
        if card[0] == "J":
            total += 10
        elif card[0] == "Q":
            total += 10
    return total


def showDealerHand(someArray):
    pass


def showPlayerHand(someArray):
    pass


def betCalculation():
    while True:
        try:
            bet = float(input("Bet Amount: "))
            if bet >= 5 and bet <= 1000:
                return bet
            else:
                print("Bet must be between $5 and $1000")
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    print(f"BLACKJACK!\nBlackjack payout is 3:2")
    money = float(db.readMoney())
    print(money)
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
    deck = generateDeck()
    print(deck)


    deck = shuffleDeck(deck)
    print("shuffled deck", deck)

    handValue = getTotalValue(HAND)
    print(handValue)


if __name__ == '__main__':
    main()


