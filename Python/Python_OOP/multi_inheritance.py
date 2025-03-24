# multiple inheritance = inherits from more than one parent class
#                        C(A, B)

# mulilevel inheritance = inherits from a parent which inherits from another parent
#                         C(B) <- B(A) <- A
#                         C is a child of B which is child of A, C is grandchild of A


class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
        

class Rabbit(Prey): 
    # Rabbits are prey and are hunted by other predators
     pass

class Hawk(Predator):
    # Hawks are predators and hunt others like rabbits
    pass

class Fish(Prey, Predator):
    # Smaller fish are preyed upon by bigger fish
    # So, they are both prey and predator
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# rabbits have flee but not hunt
rabbit.flee()

# hawks have hunt but not flee
hawk.hunt()

# Fish have both flee and hunt
fish.flee()
fish.hunt()

# As a result of multilevel inheritance
# Prey and Predator have Animal attributes
# Rabbit, Fish and Hawk also inherit Animal attributes

fish.sleep()
hawk.eat()
rabbit.sleep()