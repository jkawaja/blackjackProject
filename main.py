import decimal
import db

FILENAME = "money.txt"


def showDealerHand(someArray):
    pass

def betCalculation():
    bet = decimal.Decimal(input("Bet Amount: "))
    while True:
        try:
            if bet >= 5 and bet <= 1000:
                return bet
        except ValueError:
            print("Invalid input. Please try again.")



def main():
    print(f"BLACKJACK!\nBlackjack payout is 3:2")
    money = decimal.Decimal(db.readMoney())
    print(money)
    #
    bet = betCalculation()
    money -= bet
    db.writeMoney(money)
    print(money)



if __name__ == '__main__':
    main()


