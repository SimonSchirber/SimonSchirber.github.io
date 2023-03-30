
import math
import hashlib
#modulus for public and private key
n = 988082649547634539735932714787069852964949779
#publie key exponent
e = 65537
#random large prime number
q = 35742549198872617291353508656626642567

#Encrypted text (decimal to ASCII for resulting message)
c = 327097033161733906765917941890866428911800925



##Solution
#n is modulus of public key, derived from p and q
p = n//q

#totient
phi = (p-1) * (q - 1)


#calculate d to satisfy congruence relation, d is private key expontent
def getModInverse(e, phi):
    if math.gcd(e, phi) != 1:
        return None
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phi

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % phi

d = getModInverse(e, phi)

#c^d = m mod(n)   so we can compute m = c^d *mod n
m = pow(c,d,n)
print(m)
##answer shoule be 104971151043239821111219910139, put into decimal to ascii tool

## result says hash 'Royce'
str_to_hash = 'Royce'
result = hashlib.sha256(str_to_hash.encode())


  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())