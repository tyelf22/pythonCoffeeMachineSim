class Product:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        print(self.price)

    def make(self):
        print(f"Making {self.name}:")
        print("\tDispensing cup")
        for rec in self.recipe:
            print("\tDispencing", rec)


# test = Product("white", 1.00, ['coffee', 'sugar', 'creamer', 'water'])

# test.getPrice()

# test.make()

class Selector:
    def __init__(self, choice):
        self.choice = choice

    def select(self):
        if self.choice == 1:
            prod = Product("black", 0.35, ["coffee","water"])
        elif self.choice == 2:
            prod = Product("white", 0.35, ["coffee", "creamer", "water"])
        elif self.choice == 3:
            prod = Product("sweet", 0.35, ["coffee", "sugar", "water"])
        elif self.choice == 4:
            prod = Product("white & sweet", 0.35, ["coffee", "sugar", "creamer" "water"])
        elif self.choice == 5:
            prod = Product("bouillon", 0.25, ["boullionPowder", "water"])
        return prod
        

# selection = Selector(3).select()

# selection.make()

class CashBox:
    def __init__(self, credit, totalReceived):
        self.credit = credit
        self.totalReceived = totalReceived

        self.coins = [0.50, 0.25, 0.10, 0.05]

    def deposit(self, amount):
        if amount in self.coins:
            self.totalReceived += amount
            return f"Depositing {amount}. You have {self.totalReceived} cents credit."
        else:
            return "Only half dollars, quarters, dimes, and nickles are accepted"

    def haveYou(self, amount):
        if self.totalReceived >= amount:
            return True
        else:
            return False    

    def deduct(self, amount):
        self.totalReceived -= amount
        return self.totalReceived

    def total(self):
        return self.totalReceived

    def returnCoins(self):
        return self.credit



# c = CashBox(0.25, 0.50)

# print(c.returnCoins())


class CoffeeMachine:
    def oneAction(self):
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents) \n 1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \nSample commands: insert 25, select 1.")
        command = input("Your command: ")

        splitCommand = command.split(" ")

        c = CashBox(0.00, 0.00)

        if splitCommand[0].lower() == "insert":
            print(c.deposit(float(splitCommand[1])))
        elif splitCommand[0].lower() == "select":
            pass
        else:
            print("Command not recognized")
            

c = CoffeeMachine()

c.oneAction()