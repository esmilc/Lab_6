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




