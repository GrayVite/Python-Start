# lambda functions are used to create functions that provide
# results only useful in one particular place and doesn't 
# really make sense to create a stand-alone function for it

from functools import reduce

# For a simple example we will create an add function
def add_1(x, y):
    return x + y 

def lamb():
    # In lambda the add_1 function can be written as
    add_1l = lambda x, y: x + y

    # Both of them will have the same result

    print(f"function: {add_1(1, 2)}")
    print(f"lambda: {add_1l(1, 2)}")

# lambda is often used as an argument to other functions
# that require args with a little formatting
# For instance for the map() function

def map_lamb():
    # The map function takes an iterable and
    # for every element of that iterable it passes it to a function
    # or in our case a lambda 
    # In the example we use lambda to square numbers in a list

    my_numbers = range(1, 11)
    squares = list(map(lambda x: x*x, my_numbers))

    print(squares)  



def filter_lamb():
    # The filter function is similar to map
    # But here it checks for boolean values
    # if a certain condition is false it will reject
    # that element, like a filter

    my_numbers = range(1, 11)
    
    # Here we use it for even numbers
    evens = list(filter(lambda x: x % 2 == 0, my_numbers))
    print(evens)



def sort_lamb():
    # It can also be passed as a key to the sorted() function

    values = [(1, 'b', 'hello'), (2, 'a', 'world'), (3, 'c', 'ok')]

    # sorting bases on the length of the word 
    sorted_values = sorted(values, key=lambda x: len(x[2]))
    print(sorted_values)


def reduce_lamb():
    # The reduce function takes two arguments
    # The first arg is a function that takes two args
    # and returns a single value
    # The second arg is an iterable
    # The reduce() applies the function to the first two
    # elements of the iterable and continues till the end
    # It then returns a single value

    numbers = range(1, 6)
    sum_of_numbers = reduce(lambda acc, x: acc + x, numbers)

    max_number = reduce(lambda x, y: x if x > y else y, numbers)

    print(f"Sum of numbers: {sum_of_numbers}")
    print(f"Max Number: {max_number}")


