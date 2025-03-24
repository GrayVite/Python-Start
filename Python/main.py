from re import match


def madlibs():
    adjective1 = input("Enter an adjective (description): ")
    noun1 = input("Enter a noun: ")
    adjective2 = input("Enter an adjective (description): ")
    verb1 = input("Enter a verb ending with -ing: ")
    adjective3 = input("Enter an adjective (description): ")

    print(f"Today I went to a {adjective1} zoo.")
    print(f"In an exhibit I saw a {noun1}")
    print(f"The {noun1} was {adjective2} and {verb1}")
    print(f"I was {adjective3}")

def math_func():
    import math 

    # Some built-in math functions
    x = 3.1415
    y = -2
    z = 5

    print(round(x)) # rounds the number to the nearest whole number
    print(abs(y)) # returns the absolute value of the number
    print(pow(y, 3)) # returns the number raised to the power of the second number
    print(max(x, y, z)) # returns the largest number
    print(min(x, y, z)) # returns the smallest number
    print()

    print("Math class: ")
    print(math.pi) # returns the value of pi
    print(math.e) # returns the value of e
    print(math.sqrt(16)) # returns the square root of the number
    print(math.ceil(x)) # returns the smallest integer greater than or equal to the number, rounds up
    print(math.floor(x)) # returns the largest integer less than or equal to the number, rounds down

def calculator():
    operator = input("Enter an operator (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        print(round(num1 + num2, 3))
    elif operator == "-":
        print(round(num1 - num2, 3))
    elif operator == "*":
        print(round(num1 * num2, 3))
    elif operator == "/":
        print(round(num1 / num2, 3))
    else:
        print("Invalid operator")
    
def weight_converter():
    weight = float(input("Enter your wieght: "))
    unit = input("Enter the unit (L) for lbs or (K) for kg: ")

    if unit.upper() == "K":
        print(f"Your weight in lbs is {round(weight * 2.20462262, 3)}")
    elif unit.upper() == "L":
        print(f"your weight in kg is {round(weight / 2.20462262, 3)}")
    else:
        print("Invalid unit: {unit}")

def temp_conversion():
    unit = input("Enter the unit (C) for Celsius or (F) for Fahrenheit: ")
    temp = float(input("Enter the temperature: "))

    if unit.upper() == "C":
        print(f"The temperature in farenheit is {round(temp * 9/5 + 32, 3)}")
    elif unit.upper() == "F":
        print(F"The temperature in Celsius is {round((temp - 32) * 5/9, 3)}")
    else:
        print(f"Invalid unit: {unit}")

def coditional_expressions():
    # Conditional expressions = A one line shortcut for an if-else statement
    # Syntax: value_if_true if condition else value_if_false

    num = 6
    user_role = "admin"

    print("Positive" if num > 0 else "Negative")

    result = "Even" if num % 2 == 0 else "Odd" # Checks is the number is odd or even
    print(result)

    access_level = "Admin" if user_role == "admin" else "Guest"
    print(access_level)

def string_methods():
    #name = input("Enter your name: ")
    #phone_num = input("Enter your phone number: ")

    #result = len(name) # returns the length of the string
    #result = name.find("a") # returns the index of the first occurence of the letter, returns -1 if not found
    #result = name.rfin("a") # returns the index of the last occurence of the letter, returns -1 if not found
    #result = name.capitalize() # returns the string with the first letter capitalized
    #result = name.upper() # returns the string in uppercase
    #result = name.lower() # returns the string in lowercase
    #result = name.isdigit() # returns True if all characters are digits, spcae character are not digits
    #result = name.isalpha() # returns True if all characters are alphabetic, space character are not alphabetic

    #result = phone_num.count("-") # returns the number of times the character appears in the string
    #phone_num = phone_num.replace("-", " ") # replaces the character with another character, here dashes with spaces

    print(help(str)) # returns the documentation for the string class, contains alot of helpful string methods

def username_exercise():
    # validate user input exercise
    # 1. Username must be at least 3 characters long
    # 2. username is no more than 12 characters long
    # 3. Username must not contain spaces
    # 4. Username must not contain digits

    username = input("Enter a username: ")

    length = len(username)

    if 12 < length < 3:
        print("Username must be between 3 and 12 characters long")
    elif  not username.find(" ") == -1: # " " in username
        print("Username must not contain spaces")
    elif not username.isalpha():
        print("Username must not contain digits")
    else:
        print(f"Welcome {username}")

def string_indexing():
    # Indexing = Accessing individual characters in a string using []
    # [start:stop:step]
    credit_card = "1234-5678-9012-3456"

    print(credit_card[0]) # returns the first character
    print(credit_card[0:4]) # returns the first 4 characters [start: end_index-1]
    print(credit_card[5:9]) # returns the second set of 4 characters
    print(credit_card[-4:]) # returns the last 4 characters
    print(credit_card[:-5]) # returns all characters except the last 5
    print(credit_card[-4:-2]) # return 34
    print(credit_card[::2]) # returns every second character

    credit_card = credit_card[::-1] # reverses the string
    credit_card = reversed(credit_card) # returns an iterator(list) that reverses the string
    print("".join(credit_card)) # joins the reversed string

def formatting_specifiers():
    # Formatting specifiers = A way to format strings using placeholders
    #format specifiers: {value:flags} 

    price1 = 3.14159
    price2 = -987.65
    price3 = 12.34
    price4 = 1234.56
    price5 = 9999999.99

    # :10 -> gives the output a width of 10 characters, extra is used by spaces, default is right aligned
    print(f"Price 1 is ${price1:10.2f}") # rounds the number to 2 decimal places, f->float
    print(f"Price 2 is ${price2:010}") # the preceeding 0, adds zero the right of the number
    print(f"Price 3 is ${price3:<10}") # the left angle bracket, left aligns the number, right angle bracket right aligns the number
    print(f"Price 4 is ${price4:^10.3f}") # the caret, centers the number
    print(f"Price 5 is ${price5:+,.2f}") # adds commas to the number, the plus sign shows the sign of the number

def compound_interest():
    # Compound Interest: A = P(1 + r/n)^(t)

    principle = 0 # P
    rate = 0 # r
    time = 0 # n

    while principle <= 0:
        principle = float(input("Enter the principle amount: "))
        if principle <= 0:
            print("Principle must be greater than 0")
    
    while rate <= 0:
        rate = float(input("Enter the rate percentage: "))
        if rate <= 0:
            print("rate must be greater than 0")

    while time <= 0:
        time = float(input("Enter the time (years): "))
        if time <= 0:
            print("time must be greater than 0")

    total = principle * pow(1 + rate/100, time)

    print(f"Balance after {time} years is ${total:,.2f}")

def countdown_timer():
    import time

    my_time = int(input("Enter the time in seconds: "))

    for x in reversed(range(0, my_time)): # range(my_time, 0, -1)
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1) # pauses the program for 1 second

    print("Times Up!")

def rectangle():
    width = int(input("Enter the columns of the rectangle: "))
    height = int(input("Enter the rows of the rectangle: "))
    symbol = input("Enter a symbol to use: ")

    for x in range(height):
        for y in range(width):
            print(symbol, end="")
        print()

def Lists():
    # Lists = [] ordered and changeable, allows duplicate members
    # https://dev.programiz.com/python-programming/methods/list/pop

    fruits = ["apple", "banana", "cherry", "orange"]

    #print(dir(fruits)) # returns all the methods and attributes of the list class
    #print(help(fruits)) # returns the documentation for the list class

    print(len(fruits)) # returns the number of items in the list
    print("apple" in fruits) # returns True if the item is in the list

    print(fruits[::-1]) # indexing is similar to strings
    for fruit in fruits:
        print(fruit, end = " ")
    print()

    fruits[0] = "mango" # changes the index item in the list, in this case index 0
    for fruit in fruits:
        print(fruit, end = " ")
    
    fruits.append("pineapple") # adds an item to the end of the list
    fruits.remove("mango") # removes the first occurence of the item in the list
    fruits.insert(0, "grapes") # adds an item at the specified index
    fruits.sort() # sorts the list in ascending order, alphabetical order
    fruits.reverse() # reverses the list
    #fruits.clear() # removes all items in the list
    print(fruits.index("pineapple")) # returns the index of the first occurence of the item in the list
    print(fruits.count("grapes")) # returns the number of times the item appears in the list

def Set():
    # Sets = {} unordered and unindexed, no duplicate members, but add() and remove() methods
    # https://www.programiz.com/python-programming/methods/built-in/frozenset

    fruits = {"apple", "banana", "cherry", "orange"}
    print(fruits)

    print(dir(fruits)) # returns all the methods and attributes of the set class
    print(help(fruits)) # returns the documentation for the set class

    print(len(fruits)) # returns the number of items in the set
    print("pineapple" in fruits) # returns True if the item is in the set

    #indexing is not possible for sets

    fruits.add("pineapple") # adds an item to the set
    fruits.remove("apple") # removes the item from the set
    fruits.pop() # removes the last item from the set, in sets random
    #fruits.clear() # removes all items from the set

    for fruit in fruits:
        print(fruit, end = " ")

def Tuple():
    # Tuple = () ordered and unchangeable, allows duplicate members, faster than lists

    fruits = ("apple", "banana", "cherry", "orange")
    print(dir(fruits)) # returns all the methods and attributes of the tuple class
    print(help(fruits)) # returns the documentation for the tuple class

    print(len(fruits)) # returns the number of items in the tuple  
    print("apple" in fruits) # returns True if the item is in the tuple

    print(fruits.index("apple")) # returns the index of the first occurence of the item in the tuple
    print(fruits.count("apple")) # returns the number of times the item appears in the tuple

    for fruit in fruits:
        print(fruit, end = " ")

def ShoppingCart():
    foods = []
    prices = []
    total = 0

    while True:
        food = input("Enter a food to buy (q to quit): ")
        if food.lower() == "q":
            break
        else:
            price = float(input(f"Enter the price of the {food}: $"))
            foods.append(food)
            prices.append(price)
        
    print("-------YOUR CART-------")
    for food in foods:
        print(f"{food:18} ${prices[foods.index(food)]:.2f}")

    for price in prices:
        total += price
    
    print("-----------------------")
    print(f"Your total is ${total:,.2f}")

def TwoD_Lists():
    # 2D Lists = [[]] a list of lists, a matrix
    
    fruits = ["apple", "orange", "banana", "coconut"]
    vegetables = ["celery", "carrots", "potatoes"]
    meats = ["chicken", "fish", "turkey"]

    groceries = [fruits, vegetables, meats]

    print(groceries) # prints all the elements in the lists

    print(groceries[0]) # prints the first list

    print(groceries[0][0]) # prints the first element in the first list

    # It's not necessary to create the lists before creating the 2D list
    # You can just create the 2D list directly by placing lists in the 2D list

    print("------------------------")

    groceries_0 = [["apple", "orange", "banana", "coconut"],
                   ["celery", "carrots", "potatoes"],
                   ["chicken", "fish", "turkey"]]

    # To print the elements in the 2D list use a for loop

    for collection in groceries_0:
        for item in collection:
            print(item, end=" ")
        print()

    # It is also possible to create a list of tuples or other combinations
    # like 2D tuples, 2D sets or other

def TwoD_Tuple():
    num_pad = ( (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9),
                ("*", 0, "#"))

    for row in num_pad:
        for num in row:
            print(num, end=" ")
        print()

def quiz_game():
    questions = ("How many elements are in the periodic table? ",
                 "What is the capital of France? ",
                 "What is the largest mammal in the world? ",
                 "Which is the most abundant gas in the Earth's atmosphere? ",
                 "Which planet in the solar system is the hottest? ")

    options = ({"A. 118", "B. 120", "C. 115", "D. 110"},
               {"A. London", "B. Paris", "C. Berlin", "D. Rome"},
               {"A. Elephant", "B. Blue whale", "C. Giraffe", "D. Lion"},
               {"A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "D. Hydrogen"},
               {"A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"})

    answers = ("A", "B", "B", "A", "A")
    guesses = []

    score = 0
    question_num = 0

    for question in questions:
        print("------------------------")
        print(question)
        for option in options[question_num]:
            print(option, end="  ")
        print()
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            print("CORRECT!")
            score += 1
        else:
            print("WRONG!")
            print(f"The correct answer is {answers[question_num]}")

        question_num += 1
    
    print("---------------------------------")
    print("------------RESULTS--------------")
    print("---------------------------------")

    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")

    print()

    print(f"Your score is {score}/{len(questions)}")

def Dictionaries():
    # dictionary = collection of {key:value} pairs
    # Ordered and changeable, no duplicate keys
    # https://www.programiz.com/python-programming/methods/dictionary

    capitals = {"USA": "Washington D.C.", "India": "New Delhi", "Russia": "Moscow", "China": "Beijing"}

    #print(dir(capitals)) # returns all the methods and attributes of the dictionary class
    #print(help(capitals)) # returns the documentation for the dictionary class

    print(capitals.get("USA")) # returns the value of the key
    print(capitals.get("Japan")) # returns None if the key is not in the dictionary

    capitals.update({"Germany": "Berlin"}) # adds a new key:value pair to the dictionary
    capitals.update({"USA": "New York"}) # updates the value of the key

    capitals.pop("China") # removes the key:value pair from the dictionary
    #capitals.clear() # removes all key:value pairs from the dictionary

    keys = capitals.keys() # returns all the keys in the dictionary
    for key in keys:
        print(key, end=" ")
    
    print()

    values = capitals.values() # returns all the values in the dictionary
    for value in values:
        print(value, end=" ")

    print()

    items = capitals.items() # returns all the key:value pairs in the dictionary, in a 2D list of tuples
    #print(items)
    for key, value in items:
        print(f"{key:8}: {value}")
        
def Concession_Stand():
    menu = {"pizza": 3.00, "nachos": 4.50, "popcorn": 6.00, "fries": 2.50,
            "chips": 3.00, "pretzel": 3.50, "soda": 2.00, "lemonade": 4.25}

    cart = []
    total = 0

    print("-----------------MENU-----------------")
    for key, value in menu.items():
        print(f"{key:8}: ${value:.2f}")
    print("-------------------------------------")

    while True:
        food = input("Select an item (q to quit): ").lower()
        if food  == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)
        elif menu.get(food) is None:
            print(f"{food} is not in meny")
    
    print("-----------YOUR ORDER----------------")
    for food in cart:
        total += menu.get(food)
        print(f"{food:8}: ${menu.get(food):.2f}")
    
    print("--------------TOTAL------------------")
    print(f"Your total is ${total:.2f}")
    
def Random():
    import random

    low = 1
    high = 100
    number = random.randint(low, high) # return a random integer in the range(start, end)
    number = random.random() # return a float between 0 and 1, takes not argument

    options = ("rock", "paper", "scissors")
    option = random.choice(options)

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    random.shuffle(cards)

    print(option)
    print(cards)

def number_guess():
    import random

    low = 1
    high = 100

    answer = random.randint(low, high)

    guesses = 0
    is_running = True

    print("Python Number Guessing Game")
    print(f"Select a number between {low} and {high}: ")

    while is_running:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1
            if guess < low or guess > high:
                print("Number out of range")
                print(f"Please selecet a number between {low} and {high}")
            elif guess < answer:
                print("Too Low! Try Again")
            elif guess > answer:
                print("Too High! Try Again")
            else:
                print(f"Correct! Thw answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False
        else:
            print("Invalid Guess")
            print(f"Please selecet a number between {low} and {high}")

def Rock_Paper_Scissors():
    import random

    options = ("rock", "scissors", "paper")
    running = True

    while running:
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ").lower()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie")
        elif player == "rock" and computer == "scissors":
            print("You Win!")
        elif player == "paper" and computer == "rock":
            print("You Win!")
        elif player == "scissors" and computer == "paper":
            print("You Win")
        else:
            print("You Lose!")

        play_again = input("Play Again? (y/n): ").lower()
        if play_again == "n":
            running = False
        elif play_again != "y" and play_again != "n":
            print("Invalid Input")
            play_again = input("Play Again? (y/n): ").lower()
    
    print("Thanks for playing!")

def Dice_Roller():
    import random

    #+---------+
    #|         |
    #|    ●    |
    #|         |
    #+---------+
    # 11 columns and 5 rows
    total = 0
    dice_roll = []

    dice = {1: ("+---------+",
                "|         |",
                "|    ●    |",
                "|         |",
                "+---------+"),
            2: ("+---------+",
                "| ●       |",
                "|         |",
                "|       ● |",
                "+---------+"),
            3: ("+---------+",
                "| ●       |",
                "|    ●    |",
                "|       ● |",
                "+---------+"),
            4: ("+---------+",
                "| ●     ● |",
                "|         |",
                "| ●     ● |",
                "+---------+"),
            5: ("+---------+",
                "| ●     ● |",
                "|    ●    |",
                "| ●     ● |",
                "+---------+"),
            6: ("+---------+",
                "| ●     ● |",
                "| ●     ● |",
                "| ●     ● |",
                "+---------+")}

    dice_num = int(input("Enter your number of dice: ")) # Get the number of dice the user wants to have rolled

    # Appends dice roll number in a list
    for die in range(dice_num):
        dice_roll.append(random.randint(1, 6))

    # As there are five lines in dice ascii,
    # First generate 1st line of every ascii then 2nd and so on for respective number of dice
    for line in range(5):
        for die in dice_roll:
            print(dice.get(die)[line], end="")
        print()

    for count in dice_roll:
        total += count
    
    print(f"Total: {total}")

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

def count(end, start = 0): # non default arguments (end) should be before default arguments (start=0)
    import time

    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

def counter(seconds):
    import time

    for x in reversed(range(0, seconds)):
        sec = x % 60
        min = int((x / 60) % 60)
        hrs = int((x / 3600) % 24)
        print(f"{hrs:02}:{min:02}:{sec:02}")
        time.sleep(1)
    print("Times Up!")

def keyword_args(greeting, title, first_name, last_name):
    print(f"{greeting} {title}{first_name} {last_name}")

    # Benefit of using keyword arguments is that the order doesn't matter
    # In positional arguments messing up the order can lead to errors
    # However, make sure that all keyword arguments are placed after positional arguments
    # It helps with readability

#keyword_args("Hello", title="Mr. ", first_name="Spongebob", last_name="Squarepants")

def get_phone(country_code, area_code, first, last): #keyword args
    return f"{country_code} {area_code} {first} {last}"

#phone_num =  get_phone(country_code=+92, area_code=123, first=456, last=7890)
#print(phone_num)

def iterables():
    # iterables = An object or collection that returns it's elements one at a time,
    #             allowing it to be iterated over in a loop
    # This included lists, tuples, sets and dictionaries. Strings are also iterable

    numbers = [1, 2, 3, 4, 5]
    for num in reversed(numbers):
        print(num, end=" ")

    print()
    
    fruits = {"apple", "orange", "banana", "cococnut"}
    for fruit in fruits: # non-reverable
        print(fruit, end=" ")

    print()

    name = "Ayan Ahmad Khan"
    for character in name:
        print(character, end="")

    print()

    my_dictionary = {"A": 1, "B": 2, "C": 3}
    for item in my_dictionary: # returns only the keys
        print(item, end=" ")
    
    for item in my_dictionary.values(): # accesses the values in the dictionary
        print(item, end=" ")
    
    print()

    for key, value in my_dictionary.items(): # return key,value pairs in tuples
        print(f"{key} = {value}")

def List_Comprehension():
    # List Comprehension = A concise way to create lists in python
    # Compact and easier to read than traditional loops
    # [expression for value in iterable if condition]

    doubles = []
    for x in range(1, 11):
        doubles.append(x * 2)
    
    doubles_2 = [x*2 for x in range(1, 11)]

    triples = [x*3 for x in range(1, 11)]
    squares = [x*x for x in range(1, 11)]

    fruits = ["apple", "banana", "orange", "coconut"]
    fruits = [fruit.capitalize() for fruit in fruits]

    fruit_chars = [fruit[0] for fruit in fruits]
    
    numbers = [1, -2, 3, -4, 5, -6]
    positive_nums = [num for num in numbers if num >= 0]
    negative_nums = [num for num in numbers if num <= 0]

    even_nums = [num for num in numbers if num % 2 == 0]
    odd_nums = [num for num in numbers if num % 2 != 0]

    grades = [85, 42, 79, 90, 56, 61, 30]
    passing_grades = [grade for grade in grades if grade >= 60]

    print(passing_grades)

def match_case(day_of_week):
    # Match-Case statement (switch): An alternative way to using 'elif' statements
    #                                Execute a code if a value matches a 'case'
    # Benefits: Cleaner and more readable

    # Day of week
    match day_of_week:
        case 1:
            return "It is Monday"
        case 2:
            return "It is Tuesday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Saturday"
        case 7:
            return "It is Sunday"
        case _:
            return "Not a valid day"

def isWeekend():
    isWeekend = input("Enter day of week: ")
    match isWeekend:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Sunday" | "Saturday":  # | is the or logical operator
            return True
        case _: # default case
            return False

Dice_Roller()