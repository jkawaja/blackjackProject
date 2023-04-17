from decimal import Decimal, ROUND_HALF_UP
import moneyFunctions as mf
import deckFunctions as df
import db


def main():
        print(f"BLACKJACK!\nBlackjack payout is 3:2")
        print()
        playGame = "y"
        while playGame.lower() == "y":
            # Money set up
            money = Decimal(db.readMoney())
            money = mf.checkMoney(money)
            # While loop condition set up
            playerTurn = True
            dealerTurn = True
            checkBlackjack = True
            # Dealer / Player Hands
            dealerHand = []
            playerHand = []
            print()
            print(f"Money: {money} ")
            # Place your bet
            bet = mf.betCalculation(money)
            print()
            # Generate deck / Shuffle deck
            deck = df.generateDeck(df.CARDS)
            deck = df.shuffleDeck(deck)
            # While loop to check for Blackjack win
            while checkBlackjack:
                # Set up dealerHand
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
            # Player's Turn
            # Player can either hit or stand
            while playerTurn:
                playerChoice = input("Hit or stand? (hit/stand): ")
                if playerChoice.lower() == 'hit':
                    print(f"\nYOUR CARDS:")
                    df.showHand(playerHand)
                    playerHand = df.dealPlayerCard(deck, playerHand)
                    playerPoints = df.getTotalValue(playerHand)
                    dealerPoints = df.getTotalValue(dealerHand)
                    print()
                    # Player bust condition
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
            # Dealer's turn
            while dealerTurn:
                playerPoints = df.getTotalValue(playerHand)
                dealerPoints = df.getTotalValue(dealerHand)
                print(f"DEALER'S CARDS:")
                df.showHand(dealerHand)
                # If Dealer's points greater than player's points
                if dealerPoints > playerPoints:
                    print(f"\nYOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}\n")
                    print(f"Sorry. You lose.")
                    money -= Decimal(bet)
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
                # Dealer doesn't draw when points greater than 17
                elif dealerPoints >= 17 and dealerPoints < playerPoints:
                    print(f"\nYOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}\n")
                    print("Dealer stays. You win!")
                    money += Decimal(bet)
                    money = money.quantize(Decimal("1.00"), ROUND_HALF_UP)
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
                # If dealer's points < 17, draw
                elif df.getTotalValue(dealerHand) < 17:
                    dealerHand = df.dealDealerCard(deck, dealerHand)
                    print()
                    dealerPoints = df.getTotalValue(dealerHand)
                    # If points are greater than 17, dealer busts
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
                # Tie condition
                elif dealerPoints == playerPoints:
                    print(f"\nYOUR POINTS: {playerPoints}")
                    print(f"DEALER'S POINTS: {dealerPoints}\n")
                    print("Dealer stays. It's a tie. Player gets money back.")
                    db.writeMoney(money)
                    print(f"Money: {money}\n")
                    dealerTurn = False
            # Y / N to end the game
            playGame = ""
            while playGame not in ("y", "n"):
                answer = input("Play again? (y/n): ")
                print()
                if answer == "y":
                    playGame = "y"
                elif answer == "n":
                    playGame = "n"
                else:
                    print(f"\nInvalid input. Please enter 'y' or 'n'.")
        print(f"Come back soon!\nBye!")


if __name__ == '__main__':
    main()
