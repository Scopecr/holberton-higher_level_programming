#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for chr in  my_string:
        if not (chr == "C" or chr == "c"):
            new_string += chr
    return new_string
