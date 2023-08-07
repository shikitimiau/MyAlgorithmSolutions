"""
This file solves the FizzBuzz problem, which consists of the following:
    Generate a list of numbers.
    If the number is divisible by 3, replace it with "Fizz".
    If the number is divisible by 5, replace it with "Buzz".
    If the number is divisible by both 3 and 5, replace it with "FizzBuzz".

:author: Shikitimiau
"""

def fizzbuzz(length):
    """
    Function that solves the fizzbuzz problem using the modulo operator (%).

    :param length: Length of the fizzbuzz list to generate.
    :return: Prints the fizzbuzz list.
    """
    result = list(range(length))
    for i in range(length):
        n = i + 1
        if(n % 3 == 0 and n % 5 == 0):
            result[i] = 'FizzBuzz'
        elif (n % 5 == 0):
            result[i] = 'Buzz'
        elif (n % 3 == 0):
            result[i] = 'Fizz'
        else:
            result[i] = n
    print(result)


def fizzbuzz_sum(length):
    """
    Function that solves the fizzbuzz problem using simple addition, without the use of the modulo operator (%).

    :param length: Length of the fizzbuzz list to generate.
    :return: Prints the fizzbuzz list.
    """
    result = list(range(length))

    fizz_counter = 0
    buzz_counter = 0

    for i in range(length):
        fizz_counter += 1
        buzz_counter += 1
        if(fizz_counter == 3 and buzz_counter == 5):
            result[i] = 'FizzBuzz'
            fizz_counter = 0
            buzz_counter = 0
        elif(fizz_counter == 3):
            result[i] = 'Fizz'
            fizz_counter = 0
        elif(buzz_counter == 5):
            result[i] = 'Buzz'
            buzz_counter = 0
        else:
            result[i] = i + 1
    print(result)
