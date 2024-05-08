def list_and_tuple(*args):
    str_list = []
    for n in args:
        str_list.append(str(n))
    
    str_tuple = tuple(str_list)

    return str_list,str_tuple

print(list_and_tuple(34,67,55,33,12,98))