"""Python CMD program to calculate divisors of a number.
using Python version 3.12.0
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
    """
    main function for interacting with the user
    """
    while(True):
    # while loop to keep the program running

        print("Please enter a number to calculate its divisors:")
        input_Number = int(input())
        # casting the input string into integer

        result = calculate_Divisors(input_Number)
        # # passing the input_Number to the calculate_Divisors function and storing the result in result variable

        print("Divisors of ", input_Number, " are:")
        array_Printer(result)
        # passing the result to the array_Printer to print each array element in a line

        print("***********************************************************")


def calculate_Divisors(number):
    """
    function for calculating divisors of the entered number.
    @param number: the number to calculate its divisors.
    @type number: integer
    @examples: 
     >>> calculate_Divisors(25)
         [1, 5, 25]
     >>> calculate_Divisors(7)
         [1, 7]
    """
    divisors = []

    if(number != 1):
        divisors.append(1)
        # number 1 is a divisor for all numbers

    divisor = 2
    while (divisor <= number / 2):
        if(number % divisor == 0):
            divisors.append(divisor)
        divisor += 1

    divisors.append(number)
    # any number can be divided by itself.
    
    return divisors


def array_Printer(array):
    """
    function for printing each array element in a line.
    @param array: an array of elements.
    @type array: anything like integer, double and string.
    @examples: 
         array_1 = []
         array_2 = [1, 2, 3]
     >>> array_Printer(array_1)
          
     >>> array_Printer(array_2)
         1
         2
         3
    """
    for element in array:
        print(element)


if __name__ == '__main__':
    main()
    # run the main function after executing this file