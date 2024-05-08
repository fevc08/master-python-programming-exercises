class InputOutString:

    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Write a text: ")

    def print_string(self):
        print(self.text.upper())

# Test the class methods
obj = InputOutString()
obj.get_string()
obj.print_string()