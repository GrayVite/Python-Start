import random

def spin_row():
    symbols = ['🍒', '🍋', '🍉', '🔔', '⭐']

    results = [random.choice(symbols) for _ in range(3)]
    # for _ in range(3):
    #   results.append(random.choice(symbols))

    # .choice picks up random items from an iterable, it may pick up the same item multiple times

    return results

def print_row(row):
    # .join(iterable): Take our iterable and return a string joining each item using a space. For custom, place symbol in "-"
    print(" | ".join(row))
    print() 

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # Check to see if all three symbols are the same
        if row[0] == '🍒':  # As all are same we can check for any
            return bet*3
        elif row[0] == '🍉':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        elif row[0] == '🔔':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    else:
        return 0

def main():
    balance = 100
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍋 🍉 🔔 ⭐")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Place your bet amount: ")
        # Check to see if out bet has anything other than digits
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")

        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Would you like to play again (Y/n): ").upper()
        if play_again != 'Y':
            break
    
    print("*******************************")
    print("Game Over!")
    print(f"Your final balance: ${balance}")
    print("*******************************")

if __name__ == '__main__':
    main()