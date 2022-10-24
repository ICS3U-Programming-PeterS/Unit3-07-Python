#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 21, 2022
# This program asks for the users age and tells you if you could
# date their grandchild


def main():

    # display the starting message
    print("Hey so you want to marry our grandchild, I have a question for you. \n")

    # Get the users input for their age
    age_as_a_string = input("Enter your age: ")

    # try catch to make sure the input was an integer
    try:
        age = int(age_as_a_string)

        # If statement to make sure input wasn't 0 or a negative
        if age > 0:

            # if statement to make sure age is within range
            if age > 40 or age < 25:

                # if statement to check if too old or too young
                if age > 40:
                    print("\nYou are too old for my grandchild")
                elif age < 25:
                    print("\nYou are too young for my grandchild")
                else:
                    print("\n")
            else:
                print("\nYou can date my grandchild!")
        else:
            print("\nYour age cannot be zero or a negative number.")
    except ValueError:
        print("\nWhat you entered wasn't an integer.")

    # Print a final message
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
