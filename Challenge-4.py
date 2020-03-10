# Preston Hudson 11/21/19 Challenge 4 Written in Python

#1. Write a function that takes a number as input and returns that number squared.

def f(x):
    """
    returns x squared
    :param x: int.
    :return: int sum of x squared
    """
    return x ** 2

z = f(4)
print(z)

#2. Create a function that accepts a string as a parameter and prints it.

def string(x):
    """
    prints string
    :param x: string.
    :return: None
    """
    print(x)

string("Hello.")

#3. Write a function that takes three required parameters and two optional parameters.

def five_letters(a, b, c, d = 4, e = 5):
    """
    return the addition of a, b, c, d, and e.
    :param a: int.
    :param b: int.
    :param c: int.
    :optparam d: int.
    :optparam e: int.
    :return: sum of params
    """
    print(a + b + c + d + e)
    return a + b + c + d + e

five_letters(1, 2, 3)

#4. Write a program with 2 functions. The first function takes a integer then divides it by two. The second function takes the first functions output then multiplies it by 4.

def divided_by_two(x):
    """
    returns x divided by two
    :param x: int.
    :return: x / 2
    """
    return x / 2

def multiply_by_four(y):
    """
    returns y times 4
    :param y: int.
    :return: y * 4
    """
    return y * 4

y = divided_by_two(10)

result = multiply_by_four(y)

print(result)

#5. Write a function that converts a string into a float

def string_float(string):
    """
    returns a float converted from a string
    :param string: string.
    :returns number:
    """
    try:
        number = float(string)
        print(number)
        return number
    except ValueError:
        print("Input has to me string number.")

string_float("21")
string_float("Hundo.")


#Complete
