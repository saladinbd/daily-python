# Date: Oct 16, 2021
###########################################################################################################
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
#
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

###########################################################################################################

def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)

if __name__ == "__main__":
    x = input("Enter numbers: ")
    input_list = x.split(",")
    print(input_list)
    print(tuple(input_list))
