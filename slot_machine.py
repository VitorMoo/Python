MAX_LINES = 3

def deposit():
    while True:
        amount=input("how much you would like to deposit?")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("your deposit has to be more than 0")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines=input(f"enter the number of lines to bet on?{MAX_LINES} + )")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number")
    return lines





def main():
    balance=deposit()
    lines=get_number_of_lines()
    print(balance, lines)

main()