import decimal
import ReadWriteFunctions as rw

FILENAME = "money.txt"


def showDealerHand(someArray):
    pass



def main():
    print(f"BLACKJACK!\nBlackjack payout is 3:2")
    money = decimal.Decimal(rw.readMoney())
    print(money)
    bet = decimal.Decimal(input())
    money -= bet
    rw.writeMoney(money)
    print(money)



if __name__ == '__main__':
    main()


