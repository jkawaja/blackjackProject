FILENAME = "money.txt"
def readMoney():
    money = 0
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            money = line
    return money


def writeMoney(money):
    with open(FILENAME, "w") as file:
        file.write(f"{money}\n")