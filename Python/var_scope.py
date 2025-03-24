# variable scope: where a variable is visible and accessible
# scope resolution: (LEGB) Local -> Enclosed -> Global -> Built-in

# What this order means is the python chooses variables in the given order

x = 6

def local():
    # All local variables belong to that function
    # For instance x of local()
    x = 3
    print(x)
    
    def enclosed():
        # Enclosed variables are those which exist inside the parent function but not the local function
        # If enclosed() had a x of it's own it would print that x
        # If not then it will use local() x

        #x = 5
        print(x)
    
    enclosed()


def Global():
    # global variables are not resitricted to any function and can be used by all
    # if local and enclosed are not available, for instance the first x = 6

    print(x)

def Built_in():
    # Built-in variables belong to python or it's module and are last preference
    from math import e

    # For instace if we import e (natural constant) from math module and print it
    # without having an 'e' as LEG

    print(e)

    # if we do have e as LEG then that would be printed
    e = 3
    print(e)

#local()
#Global()
#Built_in()