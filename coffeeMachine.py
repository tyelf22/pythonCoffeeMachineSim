class Product:
    ''' ************* PRODUCT ************* '''
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        print(f"Making {self.name}:")
        print("\tDispensing cup")
        for rec in self.recipe:
            print("\tDispencing", rec)


class Selector:
    ''' ************* Selector ************* '''
    def __init__(self, choices):
        self.choices = choices

        print(self.choices)

    def select(self, choice):

        if choice == "1":
            val = self.choices[0]

        elif choice == "2":
            val = self.choices[1]

        elif choice == "3":
            val = self.choices[2]
  
        elif choice == "4":
            val = self.choices[3]
 
        elif choice == "5":
            val = self.choices[4]
            
        return val


class CashBox:
    ''' ************* CashBox ************* '''
    def __init__(self, credit, totalReceived):
        self.credit = credit
        self.totalReceived = totalReceived

        self.coins = [50, 25, 10, 5]

    def deposit(self, amount):
        if amount in self.coins:
            self.totalReceived += amount
            print(f"Depositing {amount}. You have {self.totalReceived} cents credit.")
            return amount
        else:
            print("We only take half-dollars, quarters, dimes, and nickels.\nCoin(s) returned.")

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
        self.totalReceived = 0
        

class CoffeeMachine:
    ''' ************* CoffeeMachine ************* '''
    def __init__(self):
        self.black = Product("black", 35, ["coffee", "water"])
        self.white = Product("white", 35, ["coffee", "creamer", "water"])
        self.sweet = Product("sweet", 35, ["coffee", "sugar", "water"])
        self.whiteSweet = Product("white & sweet", 35, ["coffee", "sugar", "creamer", "water"])
        self.bouillon = Product("bouillon", 25, ["boullionPowder", "water"])

        self.cb = CashBox(0, 0)

        self.sel = Selector([self.black, self.white, self.sweet, self.whiteSweet, self.bouillon])

    def oneAction(self):
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents) \n 1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \nSample commands: insert 25, select 1.")
        command = input("Your command: ")

        splitCommand = command.split(" ")

        if command == "quit":
            return False

        elif splitCommand[0].lower() == "insert":
            self.cb.deposit(int(splitCommand[1]))

        elif splitCommand[0].lower() == "select":
            choice = self.sel.select(splitCommand[1])
            cost = choice.getPrice()
            if self.cb.haveYou(cost):
                choice.make()
                self.cb.deduct(cost)
                print(f"Returning {self.cb.total()} cents. ") 
                self.cb.returnCoins()
            else:
                print("Sorry. Not enough money deposited.")
        elif command == "cancel":
            print(f"Returning {self.cb.total()} cents.") 
            self.cb.returnCoins()
            
        else:
            print("Invalid command.")

        return True

    def totalCash(self):
        return self.cb.total()
            

def main():
    ''' ************* Main ************* '''
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}")

if __name__ == "__main__":
    main()