FILENAME = "money.txt"
def readMoney(FILENAME):
    pass

def writeMoney(money):
    with open(FILENAME, "w") as file:
        file.write(f"{money}\n")