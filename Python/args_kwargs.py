# *args = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple keyword arguments
# * is the unpacking operator

def add(a, b):
    return a + b

def add_0(*nums):
    total = 0
    # *args places all the arguments inside a tuple
    # the name of the parameter isn't as important as the unpacking operator *
    for num in nums:
        total += num
    return total

print(add_0(1, 2, 3)) # We can pass in any number of arguments

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Herald", "Squarepants", "III")
print()


def print_address(**kwargs):
    print(type(kwargs)) # kwargs store all arguments inside a dictionary [key:value] pairs
    for keys in kwargs:
        print(f"{keys:9}: {kwargs.get(keys)}")
    #OR
    # for key, value in kwargs.items():
    #   print(f"{key:9}: {value})

print_address(street="11", sector="I-8/2", city="Islamabad", province="Federal Capital" ,zip_code="44790")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    
    print()

    if "house_no" in kwargs:
        print(f"{kwargs.get("house_no")}, {kwargs.get('street')}, {kwargs.get('sector')},")
    else:
        print(f"{kwargs.get('street')}, {kwargs.get('sector')},")
    print(f"{kwargs.get('city')} {kwargs.get('province')} {kwargs.get('zip_code')}")

shipping_label("Dr.", "Spongebob", "Herald", "Squarepants", "III",
               house_no="111", street="Street 11", sector="I-8/2", city="Islamabad", province="Federal Capital" ,zip_code="44790")