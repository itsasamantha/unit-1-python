"""
Task 0: Class We-Do

"""
class Character:

    health = 20

    def __init__(self, name):
        self.name = name

    def damage(self, dmg = 1):
        self.health = self.health - dmg

class Player(Character):
    health  = 50

    def healing(self):
        if self.health < 50:
            self.health = self.health + 1


enemy1 = Character("Balthazar")
enemy1.damage()
print(enemy1.health)
player1 = Player("sam")
print(player1.health)




"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
#a class of people
class People:

    #takes in name and age for each object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hi, my name is " + self.name)

#created object
sam = People("sam", 17)

sam.hello()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

#animal class
class Animal:

    def __init__(self, name):
        self.name = name

    #does nothing
    def speak (self):
        pass
        
class Cat(Animal):

    def speak(self):
        print("Meow")

class Dog(Animal):

    def speak(self):
        print("Woof")

#creating object
buttons = Cat("buttons")
#using the speak function ver. cat
buttons.speak()

#creating dog object
fluffy = Dog("fluffy")
#using speak function ver. dog
fluffy.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
#creating bank class
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    #adds amount to balence
    def depositing(self, amount):
        self.balance  += amount

    #subrtacts amount from balance 
    def withdrawing(self, amount):
        self.balance -= amount #td

my_acc = BankAccount("Samantha",2000)


#running the function deposit
my_acc.depositing(100)
#prints the result
print(my_acc.balance)
#running the function withdraw
my_acc.withdrawing(200)
#prints the result
print(my_acc.balance)