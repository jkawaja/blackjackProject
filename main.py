from decimal import Decimal, DecimalException, ROUND_HALF_UP
import deckFunctions as df
import db


def betCalculation(money):
    while True:
        try:
            bet = Decimal(input("Bet Amount: "))
            bet = bet.quantize(Decimal("1.00"), ROUND_HALF_UP)
            if bet < 5.0 and bet > 1000.00 and bet <= money:
                print("Bet must be between $5 and $1000, and less than pot. Try again.")
            else:
                return bet
        except (ValueError, DecimalException):
            print("Invalid input. Please try again.")


def checkMoney(money):
    addMoney = ""
    if money < 5:
        print("You have $0.")
        while addMoney != "y":
            addMoney = input("Would you like to buy more chips? (100) (y/n): ")
            if addMoney.lower() == "y":
                money += Decimal(100.0)
                money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                db.writeMoney(money)
            elif addMoney.lower() == "n":
                playGame = "n"
                print()
                print("You do not have enough money to bet. Game over.")
                return playGame


def main():
        print(f"BLACKJACK!\nBlackjack payout is 3:2")
        money = Decimal(db.readMoney())
        print()
        checkMoney(money)
        playGame = "y"
        while playGame.lower() == "y":

            money = Decimal(db.readMoney())
            checkMoney(money)
            money = Decimal(db.readMoney())

            playerTurn = True
            dealerTurn = True
            checkBlackJack = True
            #Dealer / Player Hands
            dealerHand = []
            # dealerHand = [["Heart", "King", 10], ["Heart", "Ace", 11]]
            playerHand = []
            # playerHand = [["Heart", "King", 10], ["Heart", "Ace", 11]]
            print()
            print(f"Money: {money} ")
            #Place your bet
            bet = betCalculation(money)
            print()
            #generate deck / shuffle deck
            deck = df.generateDeck(df.CARDS)
            deck = df.shuffleDeck(deck)
            while checkBlackJack:
            #set up dealerHand
                dealerHand = df.dealDealerCard(deck, dealerHand)
                dealerHand = df.dealDealerCard(deck, dealerHand)
                dealerPoints = df.getTotalValue(dealerHand)
                print("DEALER'S SHOW CARD:")
                df.showDealerHand(dealerHand)
                print()
                if dealerPoints == 21:
                    print("DEALER'S SHOW CARDS:")
                    df.showHand(dealerHand)
                    print()
                    print(f"Dealer Blackjack! You lose.")
                    money -= Decimal(bet)
                    money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    dealerTurn = False
                    playerTurn = False
                    print()
                    break
                # set up playerHand
                print(f"YOUR CARDS:")
                playerHand = df.dealPlayerCard(deck, playerHand)
                playerHand = df.dealPlayerCard(deck, playerHand)
                print()
                playerPoints = df.getTotalValue(playerHand)
                if playerPoints == 21:
                    print(f"YOUR CARDS:")
                    df.showHand(playerHand)
                    print()
                    print(f"Blackjack! Blackjack payout is 3:2 of bet.")
                    money += Decimal(bet) * Decimal(1.5)
                    money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    dealerTurn = False
                    playerTurn = False
                    print()
                    break
                if dealerPoints and playerPoints != 21:
                    break
                print()
            while playerTurn:
                playerChoice = input("Hit or stand? (hit/stand): ")
                print()
                if playerChoice.lower() == 'hit':
                    print(f"YOUR CARDS:")
                    df.showHand(playerHand)
                    playerHand = df.dealPlayerCard(deck, playerHand)
                    playerPoints = df.getTotalValue(playerHand)
                    dealerPoints = df.getTotalValue(dealerHand)
                    print()
                elif playerPoints > 21:
                    print()
                    print(f"YOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}")
                    print("You busted. Sorry, you lose.")
                    print()
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
                playerPoints = df.getTotalValue(playerHand)
                dealerPoints = df.getTotalValue(dealerHand)
                print(f"DEALER'S CARDS:")
                df.showHand(dealerHand)
                print()
                if dealerPoints > playerPoints:
                    print(f"YOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}")
                    print()
                    print(f"Sorry. You lose.")
                    money -= Decimal(bet)
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    print()
                    dealerTurn = False
                elif dealerPoints >= 17 and dealerPoints < playerPoints:
                    print(f"YOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}")
                    print()
                    print("Dealer stays. You win!")
                    money += Decimal(bet)
                    money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    print()
                    dealerTurn = False
                elif df.getTotalValue(dealerHand) < 17:
                    dealerHand = df.dealDealerCard(deck, dealerHand)
                    dealerPoints = df.getTotalValue(dealerHand)
                    print("DEALER'S CARDS")
                    df.showHand(dealerHand)
                    print()
                    if dealerPoints > 21:
                        print(f"YOUR POINTS: {playerPoints}")
                        print(f"DEALER'S POINTS: {dealerPoints}")
                        print()
                        print("Dealer busted. You win.")
                        money += bet
                        money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                        db.writeMoney(money)
                        print(f"Money: {money}")
                        print()
                        dealerTurn = False
                elif dealerPoints == playerPoints:
                    print()
                    print(f"YOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}")
                    print()
                    print("Dealer stays. It's a tie. Player gets money back.")
                    db.writeMoney(money)
                    print(f"Money: {money}")
                    print()
                    dealerTurn = False
            playGame = ""
            while playGame not in ("y", "n"):
                answer = input("Play again? (y/n): ")
                if answer == "y":
                    playGame = "y"
                elif answer == "n":
                     playGame = "n"
                else:
                    print()
                    print("Please enter (y/n)")
        print(f"Come back soon!\nBye!")


if __name__ == '__main__':
    main()
