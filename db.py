import sys


def readMoney():
    money = 0
    try:
        with open("money.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                money = line
    except FileNotFoundError:
        print(f"Could not find the file named 'money.txt'. Starting from Scratch\n")
        sys.exit(1)
    except Exception as e:
        print("Unknown exception. Closing program.")
        print(type(e), e)
        sys.exit(1)
    return money


def writeMoney(money):
    try:
        with open("money.txt", "w") as file:
            file.write(f"{money}")
    except FileNotFoundError:
        print(f"Could not find the file named 'money.txt'. Starting from Scratch\n")
        sys.exit(1)
    except Exception as e:
        print("Unknown exception, closing program.")
        print(type(e), e)
        sys.exit(1)
