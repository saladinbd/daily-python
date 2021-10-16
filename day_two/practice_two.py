# Date: Oct 16, 2021
###########################################################################################################
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
###########################################################################################################

class IOString(object):
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input()
    
    def print_string(self):
        print(self.text)


if __name__ == "__main__":
    my_obj = IOString()
    my_obj.get_string()
    my_obj.print_string()
