# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             pass the base function as an argument to the decorator



# This is the basic structure of a decorator
def add_sprinkles(func): # A function will be passed to the function/decorator before the one it is placed
  # The wrapper is a necessary function
  # If not present, as soon as the decorator is called the commandes
  # inside the decorator will be called
  #def wrapper(): #if we pass the wrapper func without args, it will give type error as base function has args
  # To make sure any number of arguments can be passed we use *args and **kwargs
  def wrapper(*args, **kwargs):
    print("*You add sprinkles 🎊") # The star means decorator
    func(*args, **kwargs) # Passing arguments to the base function
  return wrapper

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("*You add fudge 🍫")
    func(*args, **kwargs)
  return wrapper


# We can add more than one decorator to our base function
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
  print(f"Here is your {flavor} ice cream 🍦")


# We have extended the functionality of our base function 
# without modifying it 
get_ice_cream("chocolate")