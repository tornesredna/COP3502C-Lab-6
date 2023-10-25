
def decode(password):
    print()


def encode(password):
    print()


password_input = 12345678
menu_input = 0
while menu_input != 3:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    menu_input = int(input("Please enter an option: "))

    if menu_input == 1:
        password_input = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")

    if menu_input == 2:
        print("The encoded password is", encode(password_input), ", and the original password is", password_input)

    if menu_input == 3:
        break
