# Date: Oct 15, 2021
###########################################################################################################
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
###########################################################################################################

def solution_with_loop():
    for i in range(2000, 3200):
        if (not (i % 7)) and (i % 5):
            print(i, end=",")
    print("\b")

if __name__ == "__main__":
    solution_with_loop()
