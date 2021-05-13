#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: May 2021
# This program uses a for loop


def main():
    # this function uses a for loop

    # this is to keep track of how many times you go through the loop
    loop_counter = 0
    square = 0

    # input
    integer_as_string = input("Enter a positive integer: ")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number > 0:

            for loop_counter in range(integer_as_number + 1):
                square = loop_counter**2
            print("{0}² = {1}.".format(loop_counter, square))
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
