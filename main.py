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


def betCalculation():
    while True:
        try:
            bet = decimal.Decimal(input("Bet Amount: "))
            if bet >= 5 and bet <= 1000:
                return bet
            else:
                print("Bet must be between $5 and $1000")
        except ValueError:
            print("Invalid input. Please try again.")

def dealCard(deck, hand):
    if deck[0][1] == "Ace":
        total = getTotalValue(hand) + 11
        if total > 21 and deck[0][1] == "Ace":
            deck[0][2] = 1
        elif deck
        aceChoice = input("You have drawn an ace")
    hand.append(deck[0])
    deck.pop(0)
    return hand



def main():
        print(f"BLACKJACK!\nBlackjack payout is 3:2")
        money = decimal.Decimal(db.readMoney())
        playGame = "y"

        while playGame.lower() == "y":
            #Dealer / Player Hands
            dealerHand = []
            playerHand = []

            print(f"Money: {money}: ")
            #Place your bet
            bet = betCalculation()

            #generate deck
            deck = generateDeck(CARDS)
            #shuffle deck
            deck = shuffleDeck(deck)

            #set up dealerHand
            dealerHand = dealCard(deck, dealerHand)
            dealerHand = dealCard(deck, dealerHand)
            print("DEALER'S SHOW CARD:")
            showDealerHand(dealerHand)
            print()
            #set up playerHand
            playerHand = dealCard(deck, playerHand)
            playerHand = dealCard(deck, playerHand)
            print(f"YOUR CARDS:")
            showHand(playerHand)
            print()
            while True:
                playerChoice = input("Hit or stand? (hit/stand): ")
                if playerChoice.lower() == 'hit':
                    playerHand = dealCard(deck, playerHand)
                    print(f"YOUR CARDS:")
                    showHand(playerHand)
                elif playerChoice.lower() == "stay":
                    #PLAYERTURN = FALSE/OVER
                    #MOVE TO DEALER'S TURN

            # Dealer's Turn
            while True:

                print(f"DEALER'S CARDS:")
                showHand(dealerHand)
                #IF STATEMENT: if value of dealer's hand > value of player's hand
                    #GAME OVER, DEALER WINS
                    #SORRY. YOU LOSE.
                    #SUBTRACT MONEY FROM PLAYER POT, SHOW PLAYER POT
                    # CHECK IF PLAYER POT < $5. IF SO, PLAYER HAS OPTION TO BUY MORE CHIPS


    playGame = input("Play again? (y/n): ")










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


