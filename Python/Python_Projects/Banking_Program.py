
def show_balance(Balance):
    print("****************************")
    print(f"Your balance is: ${Balance:.2f}")
    print("****************************")

def deposit():
    print("****************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("****************************")
    if amount <= 0:
        print("****************************")
        print("That's not a valid amount")
        print("****************************")
        return 0
    else:
        return amount

def withdraw(Balance):
    print("****************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("****************************")
    if amount > Balance:
        print("****************************")
        print("Insufficient funds")
        print("****************************")
        return 0
    elif amount < 0:
        print("****************************")
        print("Amount must be greater than zero")
        print("****************************")
        return 0
    else:
        return amount

def main():
    Balance = 0
    is_running = True

    while is_running:
        print("****************************")
        print("       Banking Program      ")
        print("****************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************************")

        choice = input("Enter your choice (1-4): ")
        match choice:
            case '1':
                show_balance(Balance)
            case '2':
                Balance += deposit()
            case '3':
                Balance -= withdraw(Balance)
            case '4':
                is_running = False
            case _:
                print("****************************")
                print("That is not a valid choice")
                print("****************************")

    print("****************************")
    print("Thank you, have a nice day!")
    print("****************************")

if __name__ == '__main__':
    main()