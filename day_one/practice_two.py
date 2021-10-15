# Date: Oct 15, 2021
###########################################################################################################
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
###########################################################################################################

def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    
    print(calc_factorial(x))
