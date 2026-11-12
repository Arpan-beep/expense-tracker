def menu():
    print('\n')
    print('\t\t\t\t------Welcome to the expense Tracker-------\n')
    while True:
        print('1) Add expense')
        print('2) View all expenses')
        print('3) Filter and search')
        print('4) Display spending Summary')
        print('5) Remove expenses')
        print('6) Edit expenses')
        print('0) Exit \n')
        try:
            option = int(input('Please select your option(0-6): '))
        except:
            option =10 

        match option:
            case 0:
                print('\t\t--------Goodbye!!!!!! :)')
                break
            case 1:
                add_expense()
            case 2:
                print("System paused.")  
            case _:
                print("\n\t\t\t -------Invalid input. Please enter a whole number.(0-6)-----")


def add_expense():
    try:
        amount=float(input('\nEnter the amount allocated for this expense'))
    except:
        print('Enter an amount in numbers with or with decimal points')

def main():
    menu()

if __name__ == '__main__':
    main()