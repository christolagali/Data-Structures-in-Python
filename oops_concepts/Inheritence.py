
# PArent class
class Dog(object):

    # class Attribute
    species = "Mammal"

    # INstance Attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name,self.age)
    
    # instance methods
    def speak(self,sound):
        return "{} says {}".format(self.name,sound)
    


# Child class inherits from Dog class
class RussellTerrier(Dog):

    def run(self,speed):
        return "{} runs at speed {}".format(self.name,speed)
    
# Child class inherits from Dog class
class Bulldog(Dog):

    def run(self,speed):
        return "{} runs {} fast ".format(self.name,speed)


##########Overriding functionality of parent class

class otherSpecies(Dog):
    species = "Reptile"


# Child classes inherit attributes and
# behaviors from the parent class
benny = Bulldog("Benny",12)

print(benny.run(30))


# check if benny is an instance of Dog class

print(isinstance(benny,Dog))


# new instance of Dog class
julie = RussellTerrier("Julie",8)
print(julie.run("Fast"))


print(isinstance(julie,Dog))


pepper = otherSpecies("Pepper",5)

print(pepper.age)

print(pepper.speak("croak"))

print(pepper.species)
