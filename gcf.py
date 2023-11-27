#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: November 25, 2023
# This program asks the user to enter two or three numbers,
# it then tells them the greatest common factor.


def main():
    counter = 1
    num_amount = "0"

    # Initial Greeting.
    print("Hello and welcome to my program.")
    print("In a second, you will be asked to input numbers, ")
    print("and I'll tell you the greatest common factor.")
    print("Before we begin, how many numbers would you like the gcf of, 2 or 3?")

    # Uses loop to get amount of numbers from user.
    while num_amount != "2" and num_amount != "3":
        num_amount = input("Enter num_amount: ")
        if num_amount != "2" and num_amount != "3":
            print("Please enter 2 or 3!")

    # Gets numbers as strings from user.
    num_str_1 = input("Enter num_str_1: ")
    try:
        num_int_1 = int(num_str_1)
        num_str_2 = input("Enter num_str_2: ")
        try:
            num_int_2 = int(num_str_2)

            # Extra functionality - GCF of 3 numbers if wanted.
            if num_amount == "3":
                num_str_3 = input("Enter num_str_3: ")
                try:
                    num_int_3 = int(num_str_3)
                    # Uses loop to calculate greatest common factor.
                    while (
                        counter <= num_int_1
                        and counter <= num_int_2
                        and counter <= num_int_3
                    ):
                        if (
                            num_int_1 % counter == 0
                            and num_int_2 % counter == 0
                            and num_int_3 % counter == 0
                        ):
                            gcf = counter
                        counter += 1
                    # Displays greatest common factor.
                    print(f"The greatest common factor is {gcf}.")
                except ValueError:
                    print(f"{num_str_3} is not a number.")
            else:
                # Uses loop to calculate greatest common factor.
                while counter <= num_int_1 and counter <= num_int_2:
                    if num_int_1 % counter == 0 and num_int_2 % counter == 0:
                        gcf = counter
                    counter += 1
                # Displays greatest common factor.
                print(f"The greatest common factor is {gcf}.")
        except ValueError:
            print(f"{num_str_2} is not a number.")
    except ValueError:
        print(f"{num_str_1} is not a number.")


if __name__ == "__main__":
    main()
