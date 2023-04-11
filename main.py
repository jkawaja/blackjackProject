import db

FILENAME = "money.txt"

# The type of suit
suits = ["♠", "♥", "♦", "♣"]
# The face value of the card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def functionThatGetsFaceValue():
    pass

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
    money = db.readMoney()
    print(money)
    #test subtract money
    print("Test Subtract Money")
    bet = betCalculation()
    money = money - bet
    db.writeMoney(money)
    print(money)

    #add money test
    print("Test Add Money")
    bet = betCalculation()
    money = money + bet
    db.writeMoney(money)
    print(money)



if __name__ == '__main__':
    main()


