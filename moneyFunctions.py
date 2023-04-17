from decimal import Decimal, DecimalException, ROUND_HALF_UP
import db

# Checks to see if bet is < than current funds. See if it's between 5 and 1000.
# Quantize to make sure result is rounded to 2 decimal points.
def betCalculation(money):
    while True:
        try:
            bet = Decimal(input("Bet Amount: "))
            if bet > money:
                print(f"Bet cannot be greater than available funds.\nPlease try again.")
            elif bet < Decimal(5) or bet > Decimal(1000):
                print(f"Bet must be between $5 and $1000.\nPlease try again.")
                continue
            else:
                bet = bet.quantize(Decimal("1.00"), ROUND_HALF_UP)
                return bet
        except (ValueError, DecimalException):
            print("Invalid input. Please try again.")

# Check to see if there is enough money to bet
# If not, offer player to buy more chips. Exit program if they say no.
def checkMoney(money):
    addMoney = ""
    while money < 5:
        print("You have $0.")
        while addMoney != "y":
            addMoney = input("Would you like to buy more chips? (100) (y/n): ")
            if addMoney.lower() == "y":
                money += Decimal(100.0)
                money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                db.writeMoney(money)
                return money
            elif addMoney.lower() == "n":
                print()
                print("You do not have enough money to bet. Game over.")
                exit(1)
