import string

flag = 'thank you for playing this ucla challenge the flag for this game is bruinlearn'


alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

ciphered_string = ''

for letter in flag:
    #skip the space bar
    if letter == ' ':
        ciphered_string = ciphered_string + ' '
        continue
    #check for index of letter
    for index, table in enumerate(alphabet_list):
        if letter == table:
            cipher_index = index + 4
            try:
                ciphered_string = ciphered_string + alphabet_list[cipher_index]
            #if at the end loop back to beggining
            except:
                ciphered_string = ciphered_string + alphabet_list[cipher_index -26]
            break
        else:
            continue


print(f'The Cipher text is {ciphered_string}')