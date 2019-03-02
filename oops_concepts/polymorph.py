
# Parrot class
class parrot:

    def __init__(self,name):
        self.name = name
    
    def swim(self):
        return "{} cannot swim".format(self.name)

    def fly(self):
        return "{} can fly".format(self.name)

# penguine Class
class Penguine:

    def __init__(self,name):
        self.name = name
    
    def swim(self):
        return "{} can swim".format(self.name)

    def fly(self):
        return "{} cannot fly".format(self.name)

# common interface
def flying_test(bird):
    return bird.fly()


bobby = parrot("Bobby")

jenna = Penguine("Jenna")

# passing the object
#print(flying_test(bobby))
#print(flying_test(jenna))


# Polymorphism with Class Methods

""" 
To show how Python can use each of these different class types in the same way, 
we can first create a for loop that iterates through a tuple of objects. 
Then we can call the methods without being concerned about which class type each object is. 
We will only assume that these methods actually exist in each class. 
"""

for bird in (bobby,jenna):

    print(bird.fly())
    print(bird.swim())



# Polymorphism with a Function

"""
We can also create a function that can take any object, allowing for polymorphism.

Let’s create a function called in_the_pacific() which takes in an object we can call fish. 
Though we are using the name fish, any instantiated object will be able to be called into this function:
"""

def in_the_pacific(fish):
    return fish.swim() , "in the pacific"


for fish_obj in (bobby,jenna):
    print(in_the_pacific(fish_obj))



