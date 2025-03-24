# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.excpet, 3.finally 

# Any code that is considered dangerous is places inside a try block
# For example, when accepting user input, cause the user can enter anything

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero, IDIOT!")
except ValueError:
    print("Enter only numbers please")
except Exception:
# It's bad practice to just Exception to catch all exceptions
    print("Something went wrong")
# The finally block runs, regardless of whether an expetion was caught or not
finally:
    print("Do some clean-up")