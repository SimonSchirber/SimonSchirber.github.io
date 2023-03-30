
import rsa
import math


#number inserted is keylength
publicKey, privateKey = rsa.newkeys(1024)
message = "hash 'Royce'"

p =27644437
q = 35742549198872617291353508656626642567
n = p * q
print("n is" + str(n))

#totient(n) = (p-1)(q-1)
totient = (p-1) * (q-1)

#print(f'totient: {totient}')

#e must be less than totient = 44422408 
e = 65537

# d = e^-1 * mod(totient) or 
###### Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

# application of Extended Euclidean Algorithm to find a modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m
####
#d = modinv( e, totient)
d = modinv(e, totient)
#check with d that function is equal to one 
#print(f'Works if equal to 1: {pow(e*d, 1, totient)}')


#Convert message String to Decimal concatonating ascii decimal range [32, 122]
dec_message = ''
for letter in message:
    dec_message += str(ord(letter))
print(dec_message)

m = int(dec_message)

#ciphered message
#C = M^e mod(n)
#c = pow(m, e, n)
c = pow(m, e, n)
print('c is ' + str(c))


#message from ciphered text
#to decrypt use M = C^d mod (n)
decipered_m = pow(c,d,n)



