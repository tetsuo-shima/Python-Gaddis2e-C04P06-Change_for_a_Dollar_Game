__author__ = 'dwight'

#Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The
# program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total value of
# the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise,
# the program should display a message indicating whether the amount entered was more than or less than one dollar.


def main():
    dollar_value = 100

    print('Change for a Dollar Game')
    print('========================')
    pennies = int(input('Enter number of pennies: '))
    nickels = int(input('Enter number of nickles: '))
    dimes = int(input('Enter number of dimes: '))
    quarters = int(input('Enter number of quarters: '))

    total_coin_value = calc_coin_value(pennies, nickels, dimes, quarters)

    print()
    if total_coin_value == dollar_value:
        print("Congratulations! You made a dollar!")
    elif total_coin_value > dollar_value:
        print("Sorry! Your coins add up to more than $1.")
    else:
        print("Sorry! Your coins add up to less than $1.")



def calc_coin_value(pennies, nickels, dimes, quarters):
    return pennies + calc_nickels_value(nickels) + calc_dimes_value(dimes) + calc_quarters_value(quarters)


def calc_nickels_value(coins):
    coin_value = 5
    return coins * coin_value


def calc_dimes_value(coins):
    coin_value = 10
    return coins * coin_value


def calc_quarters_value(coins):
    coin_value = 25
    return coins * coin_value


main()