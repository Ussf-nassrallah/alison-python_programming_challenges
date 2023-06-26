import sys

"""
1 - Write a function that prints x elements of a list.

    Prototype: def safe_print_list(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All elements must be printed on the same line followed by a new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    You have to use try: / except:
    You are not allowed to import any module
    You are not allowed to use len()

"""


def safe_print_list(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print("{}".format(my_list[index]), end="")
            count = count + 1
        except IndexError:
            break
    print()
    return count


"""
2- Write a function that prints an integer with "{:d}".format().

    Prototype: def safe_print_integer(value):
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to import any module
    You are not allowed to use type()
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


"""
Write a function that prints the first x elements of a list and only integers.

    Prototype: def safe_print_list_integers(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
    Returns the real number of integers printed
    You have to use try: / except:
    You have to use "{:d}".format() to print an integer
    You are not allowed to import any module
    You are not allowed to use len()
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count = count + 1
        except (ValueError, TypeError):
            continue
    print()
    return count


"""
4- Write a function that divides 2 integers and prints the result.

    Prototype: def safe_print_division(a, b):
    You can assume that a and b are integers
    The result of the division should print on the finally: section preceded by Inside result:
    Returns the value of the division, otherwise: None
    You have to use try: / except: / finally:
    You have to use "{}".format() to print the result
    You are not allowed to import any module
"""


def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))


"""
Write a function that divides element by element 2 lists.

    Prototype: def list_division(my_list_1, my_list_2, list_length):
    my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements can’t be divided, the division result should be equal to 0
    If an element is not an integer or float:
    print: wrong type
    If the division can’t be done (/0):
    print: division by 0
    If my_list_1 or my_list_2 is too short
    print: out of range
    You have to use try: / except: / finally:
    You are not allowed to import any module
"""


def list_division(my_list_1, my_list_2, list_length):
    length = list_length
    new_list = []
    for index in range(0, length):
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list


"""
Write a function that prints an integer.

Prototype: def safe_print_integer_err(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False and prints in stderr the error precede by Exception:
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to use type()
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False

