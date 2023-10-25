# Tor andersen, edited by jack detweiler
def decode(password):
    new_password = ""
    for i in range(0, len(password)):
        new_char = int(password[i]) - 3
        if new_char < 0:
            new_password = new_password + (str(new_char)[-1])
        else:
            new_password = new_password + str(new_char)
    return new_password

def encode(password):
    new_password = ""
    for i in range(0, len(password)):
        new_char = int(password[i]) + 3
        if new_char >= 10:
            new_password = new_password + (str(new_char)[-1])
        else:
            new_password = new_password + str(new_char)
    return new_password


password_input = 12345678
menu_input = 0
while menu_input != 3:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    menu_input = int(input("Please enter an option: "))

    if menu_input == 1:
        password_input = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n")

    if menu_input == 2:
        print("The encoded password is " + encode(password_input) + ", and the original password is " + password_input + ".\n")

    if menu_input == 3:
        break
