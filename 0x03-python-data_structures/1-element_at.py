#!/usr/bin/python3
def element_at(my_list, idx):
   for i in my_list:
       if idx < i in my_list:
          print("None")
       elif idx > i in my_list:
          print("None")
       else:
          print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))  
