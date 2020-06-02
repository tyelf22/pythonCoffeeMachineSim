''' Tyson Elfors
6/3/20
CS-1410
Project 4 - Coffee Machine
'''

"""I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitues cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""

class Product:
    ''' creates new coffee product given the name, price, and list includes ingredients '''
    def __init__(self, name, price, recipe):
        ''' initialize with name, price, recipe '''
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        ''' returns the price of product '''
        return self.price

    def make(self):
        ''' returns string format for recipe '''
        print(f"Making {self.name}:")
        print("\tDispensing cup")
        for rec in self.recipe:
            print("\tDispencing", rec)


class Selector:
    ''' ************* Selector ************* '''
    def __init__(self, choices):
        ''' initializes which product the user chose '''
        self.choices = choices

    def select(self, choice):
        ''' set val to correct product object '''
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
        ''' initializes credit and total received amounts '''
        self.credit = credit
        self.totalReceived = totalReceived

        self.coins = [50, 25, 10, 5] #restrict user input to half dollars, quarters, dimes, nickels

    def deposit(self, amount):
        ''' Depost given amount and add to the totalReceived'''
        if amount in self.coins:
            self.totalReceived += amount #accumulator
            print(f"Depositing {amount}. You have {self.totalReceived} cents credit.")
            return amount
        else:
            print("We only take half-dollars, quarters, dimes, and nickels.\nCoin(s) returned.")

    def haveYou(self, amount):
        ''' test for determining if the user has enough money '''
        if self.totalReceived >= amount:
            return True
        else:
            return False    

    def deduct(self, amount):
        ''' deduct the cost of the user selection for totalReceived'''
        self.totalReceived -= amount #accumulator
        return self.totalReceived

    def total(self):
        ''' current total '''
        return self.totalReceived

    def returnCoins(self):
        ''' set total to 0 '''
        self.totalReceived = 0
        

class CoffeeMachine:
    ''' ************* CoffeeMachine ************* '''
    def __init__(self):
        ''' initialize the products, cashbox, and selector. It passes the list of Product objects to the Selector constructor. '''
        self.black = Product("black", 35, ["coffee", "water"])
        self.white = Product("white", 35, ["coffee", "creamer", "water"])
        self.sweet = Product("sweet", 35, ["coffee", "sugar", "water"])
        self.whiteSweet = Product("white & sweet", 35, ["coffee", "sugar", "creamer", "water"])
        self.bouillon = Product("bouillon", 25, ["boullionPowder", "water"])

        self.cb = CashBox(0, 0)

        self.sel = Selector([self.black, self.white, self.sweet, self.whiteSweet, self.bouillon])

    def oneAction(self):
        ''' Receives user input and references each class object '''
        
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents) \n 1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \nSample commands: insert 25, select 1.")
        command = input("Your command: ")

        splitCommand = command.split(" ") #split the user input to differentiate each command

        #if elif chain to handle user input
        if command == "quit": 
            return False

        elif splitCommand[0].lower() == "insert":
            self.cb.deposit(int(splitCommand[1])) #deposit to cash box

        elif splitCommand[0].lower() == "select":
            choice = self.sel.select(splitCommand[1])
            cost = choice.getPrice() #get price of user selected product
            if self.cb.haveYou(cost): #check if user has enough money for product
                choice.make() #make the product
                self.cb.deduct(cost) #deduct cost of product from total 
                print(f"Returning {self.cb.total()} cents. ") #returned coins
                self.cb.returnCoins() #set total to 0
            else:
                print("Sorry. Not enough money deposited.")
        elif command == "cancel":
            print(f"Returning {self.cb.total()} cents.")  #amount of coins returned
            self.cb.returnCoins()
            
        else:
            print("Invalid command.")

        return True # continue returning true to loop function

    def totalCash(self):
        ''' current total '''
        return self.cb.total()
            

def main():
    ''' ************* Main ************* '''
    m = CoffeeMachine() # create object from CoffeeMachine class
    while m.oneAction(): # loop through oneAction method
        pass
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}") #format total for when user quits

if __name__ == "__main__":
    main()