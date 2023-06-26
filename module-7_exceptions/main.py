from exceptions import *

# my_list = [1, 2, 3, 4, 5]
#
# nb_print = safe_print_list(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))

# value = 89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
#
# value = -89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
#
# value = "School"
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))


# my_list = [1, 2, 3, 4, 5]
#
# nb_print = safe_print_list_integers(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
#
# my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
# nb_print = safe_print_list_integers(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
#
# nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))

# a = 12
# b = 2
# result = safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))
#
# a = 12
# b = 0
# result = safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))

# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)
#
# print("--")
#
# my_l_1 = [10, 8, 4, 4]
# my_l_2 = [2, 0, "H", 2, 7]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))