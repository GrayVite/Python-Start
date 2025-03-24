# Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time
# We will be using the time module to simulate the functions taking alot of time

def walk_dog(first_name, last_name):
    time.sleep(8) # 8 seconds
    print(f"You finish walking {first_name} {last_name}")

def take_out_trash():
    time.sleep(2)
    print(f"You take out the trash")

def get_mail():
    time.sleep(4)
    print(f"You get the mail")

if __name__ == "__main__":
    # These function run one after the other and take up alot of time
    # Using threading they would execute side by side

    # walk_dog()
    # take_out_trash()
    # get_mail()

    # As the time for each function is different, they will end at different times
    # So, the function to end first is executed first
    # As a result they may not appear in order

    # If our function contsins then we need to pass a argument called args
    # We pass a tuple containing all the arguments our function requires
    chore_1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # Place comma to let python know it's a tuple
    chore_1.start() 

    chore_2 = threading.Thread(target=take_out_trash)
    chore_2.start()

    chore_3 = threading.Thread(target=get_mail)
    chore_3.start()

    # If we do not use the .join method these the print below would finish first
    chore_1.join()
    chore_2.join()
    chore_3.join()

    print(f"All chores are complete")