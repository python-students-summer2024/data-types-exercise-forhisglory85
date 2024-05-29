"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    total_sales = int(input("Enter in the projected amount of total sales: "))
    annual_profit = total_sales * 0.23
    formatted_profit = format(annual_profit, ",.2f")
    formatted_sales = format(total_sales, ",d")
    print(f"Profit: ${formatted_profit}")
    
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """



def calculate_quotient_and_remainder():
    integer_one = int(input("Please submit an integer: "))
    integer_two = int(input("Please submit an integer: "))
    quotient = integer_one // integer_two
    remainder = integer_one % integer_two
    print(f"{integer_two} goes into {integer_one} a total of {quotient} times with a remainder of {remainder}")

    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """


def calculate_miles_per_gallon():
    miles_driven = int(input("Miles driven: "))
    gallons_used = int(input("Gas used in gallons: "))
    mpg = miles_driven / gallons_used
    print(f"Miles per gallon: {mpg:2f}")
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """


def align_text():
    price1 = float(input("Enter price #1: "))
    price2 = float(input("Enter price #2: "))
    price3 = float(input("Enter price #3: "))

    formatted_price1 = f"${price1:8.2f}"
    formatted_price2 = f"${price2:8.2f}"
    formatted_price3 = f"${price3:8.2f}"

    print("\nHere are your prices!\n")
    print(f"Price #1: {formatted_price1}")
    print(f"Price #2: {formatted_price2}")
    print(f"Price #3: {formatted_price3}")
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
