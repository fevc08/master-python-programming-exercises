# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    string_num = str(num)
    last_two_num = string_num[len(string_num)-2] + string_num[len(string_num)-1]
    return int(last_two_num)

# Invoke the function with any integer greater than 9
print(last_two_digits(3245647983))
