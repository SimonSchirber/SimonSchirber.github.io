import string

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)


##Inputs given
cipher_text = 'xlero csy jsv tpecmrk xlmw ygpe gleppirki xli jpek jsv xlmw keqi mw fvymrpievr'
shift = 4

##Create dictionary mapping together
deciphered_key = {}
for index, letter in enumerate(alphabet_list):
    if index < 4:
        deciphered_key[letter] = alphabet_list[index - 4 + 26]
    else:
        deciphered_key[letter] = alphabet_list[index - 4]

print(deciphered_key)
flag = ''

#Remove spaces and decipher 
for letter in cipher_text:
    if letter == ' ':
        flag =  flag + ' '
        continue
    flag = flag + deciphered_key[letter]

print(flag)