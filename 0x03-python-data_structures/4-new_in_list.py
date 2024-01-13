#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_list = my_list[:]
    if 0 <= idx < len(my_list):
        tmp_list[idx] = element
        return(tmp_list)
    return(my_list)

vi 5-no_c.py

#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            new_str += i
    return (new_str)

