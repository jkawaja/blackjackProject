from decimal import Decimal, ROUND_HALF_UP
import moneyFunctions as mf
import deckFunctions as df
import db





def main():
        print(f"BLACKJACK!\nBlackjack payout is 3:2")
        money = Decimal(db.readMoney())
        mf.checkMoney(money)
        playGame = "y"
        while playGame.lower() == "y":
            money = Decimal(db.readMoney())
            mf.checkMoney(money)
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
            bet = mf.betCalculation(money)
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
                    print(f"\nBlackjack! Blackjack payout is 3:2 of bet.")
                    money += Decimal(bet) * Decimal(1.5)
                    money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
                    playerTurn = False
                    break
                if dealerPoints and playerPoints != 21:
                    break
                print()
            while playerTurn:
                playerChoice = input("Hit or stand? (hit/stand): ")
                if playerChoice.lower() == 'hit':
                    print(f"\nYOUR CARDS:")
                    df.showHand(playerHand)
                    playerHand = df.dealPlayerCard(deck, playerHand)
                    playerPoints = df.getTotalValue(playerHand)
                    dealerPoints = df.getTotalValue(dealerHand)
                    print()
                    if playerPoints > 21:
                        print(f"YOUR POINTS: {playerPoints}")
                        print(f"DEALER'S POINTS: {dealerPoints}\n")
                        print(f"You busted. Sorry, you lose.\n")
                        money -= bet
                        db.writeMoney(money)
                        print(f"Money: {money}\n")
                        dealerTurn = False
                        playerTurn = False
                elif playerChoice.lower() == "stand":
                    print()
                    playerTurn = False
            while dealerTurn:
                playerPoints = df.getTotalValue(playerHand)
                dealerPoints = df.getTotalValue(dealerHand)
                print(f"DEALER'S CARDS:")
                df.showHand(dealerHand)
                if dealerPoints > playerPoints:
                    print(f"\nYOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}\n")
                    print(f"Sorry. You lose.")
                    money -= Decimal(bet)
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
                elif dealerPoints >= 17 and dealerPoints < playerPoints:
                    print(f"\nYOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}\n")
                    print("Dealer stays. You win!")
                    money += Decimal(bet)
                    money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
                elif df.getTotalValue(dealerHand) < 17:
                    dealerHand = df.dealDealerCard(deck, dealerHand)
                    print()
                    dealerPoints = df.getTotalValue(dealerHand)
                    if dealerPoints > 21:
                        print(f"DEALER'S CARDS:")
                        df.showHand(dealerHand)
                        print(f"\nYOUR POINTS: {playerPoints}")
                        print(f"DEALER'S POINTS: {dealerPoints}\n")
                        print("Dealer busted. You win.")
                        money += bet
                        money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                        db.writeMoney(money)
                        print(f"Money: {money}\n")
                        dealerTurn = False
                elif dealerPoints == playerPoints:
                    print(f"\nYOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}\n")
                    print("Dealer stays. It's a tie. Player gets money back.")
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
            playGame = ""
            while playGame not in ("y", "n"):
                answer = input("Play again? (y/n): ")
                if answer == "y":
                    playGame = "y"
                elif answer == "n":
                    playGame = "n"
                else:
                    print(f"\nInvalid input. Please enter 'y' or 'n'.")
        print(f"Come back soon!\nBye!")


if __name__ == '__main__':
    main()
