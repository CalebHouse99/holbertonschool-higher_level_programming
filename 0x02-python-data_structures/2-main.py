#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
idx = 4
new_element = 2734698236498273649872364897
new_list = replace_in_list(my_list, 2, new_element)

print(new_list)
print(my_list)