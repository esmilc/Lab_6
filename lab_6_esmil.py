# Esmil Canet

def encode(user_input):
    list_num = []
    enc_list = []
    num_str = ''
    user_input = str(user_input)
    for num in user_input:
        list_num.append(num)
    for num in list_num:
        num = int(num)
        num += 3
        enc_list.append(num)
    for num in enc_list:
        num = str(num)
        num_str += num
    return num_str

def decode(user_input):
    password = str(user_input)
    new_pass_list = []
    for num in password:
        num = int(num)
        num -= 3
        new_pass_list.append(str(num))
    new_pass = "".join(new_pass_list)
    return new_pass

def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

cont = True
while cont:
    menu()

    menu_option = input('Please enter an option: ')

    if menu_option == '1':
        user_input = input('Please enter your password to encode: ')
        global encoded_pass
        encoded_pass = encode(user_input)
        print('Your password has been encoded and stored!\n')

    elif menu_option == '2':
        decoded_pass = decode(encoded_pass)
        print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
        print()

    elif menu_option == '3':
        break












