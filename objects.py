class Parent:
    """A class representing a parent"""
    def __init__(self, fName="",lName=""):
        self.fName = fName
        self.lName = lName

    fName = ""
    lName = ""

    def printName(self):
        print("Full Name: " + self.fName + " " + self.lName)

class Mom(Parent):
    """A class representing a mom"""

    def __init__(self, fName="", lName="", dressSize=0):
        self.dressSize = dressSize
        self.fName = fName
        self.lName = lName

    dressSize = -1
        
    def printInfo(self):
        self.printName()
        print("Dress Size: " + str(self.dressSize)) 

class Dad(Parent):
    """A class representing a dad"""

    def __init__(self, fName="", lName="", numScrewdrivers=0):
        self.numScrewdrivers = numScrewdrivers
        self.fName = fName
        self.lName = lName
        
    numScrewdrivers = -1
    
    def printInfo(self):
        self.printName()
        print("Number of screwdrivers: " + str(self.numScrewdrivers))

class Pet():
    """A class representing a pet"""
    def __init__(self, name=""):
        self.name = name

    name = ""

    def printName(self):
        print('Name: ' + self.name)

class Cat(Pet):
    """A class representing a cat"""
    def __init__(self, name="", color="unknown"):
        self.name = name
        self.color = color

    color = ""

    def printInfo(self):
        self.printName()
        print('Color: ' + self.color)
        

class Dog(Pet):
    """A class representing a dog"""
    def __init__(self, name="Dog", pantingRate=-1):
        self.name = name
        self.pantingRate = pantingRate


    pantingRate = -1

    def printInfo(self):
        self.printName()
        print('Panting rate: ' + str(self.pantingRate))


# Declare test objects
testParent = Parent('Pewdie', 'Pie')
testMom = Mom('Cruella', 'Deville', 12)
testDad = Dad('Arnold', 'Schwarzeneggar', 15)
testCat = Cat('Fluffly', 'yellow and pink')
testDog = Dog('Max', 100)

# Print info about test objects
print('***Printing info about test objects***\n')
testParent.printName()
testMom.printInfo()
testDad.printInfo()
testCat.printInfo()
testDog.printInfo()


input()

