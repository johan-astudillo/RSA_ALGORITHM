#!/usr/bin/env python
# coding: utf-8


import random
import sys
import os
import time
import socket


os.system("cls")
print("Autor: Johan Fernando Astudillo")


generate_range_primes = int(input("Key Length: "))

n = generate_range_primes
primes = []

# loop for in range and get primes 
for i in range(2, n + 1):
	for j in range(2, int(i ** 0.5) + 1):        
 		if i%j == 0:            
 			break
	else:
		primes.append(i)
        
print("\n" +str (primes))


#get random primes 
p_prime = random.choice(primes)
q_prime = random.choice(primes)

n_modulus = p_prime * q_prime

print("\n"+"Private key of person B... ")
print("P Prime is: " +  str(p_prime))
print("Q Prime is: " +  str(q_prime))
print("Module N is: " + str(n_modulus))


#get euler_phi
euler_phi = (p_prime - 1) * (q_prime-1)
print("\n"+"Euler Phi is: " + str(euler_phi))


# list numbers before the euler_phi
list_number = []

for i in range (1,euler_phi):
    list_number.append(i)

print("\n"+ str(list_number))


#Get any number and valid if is co-prime, else re-execute
def get_any_co_prime():
    co_prime =  random.choice(list_number)
    if euler_phi  % co_prime == 1:
        return co_prime
    else:
        return get_any_co_prime()
    
get_co_prime = get_any_co_prime()


print(get_co_prime)

#find modular inverse
def find_mod_inv(a,m):
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x        
    raise Exception('The modular inverse does not exist.')


a = get_co_prime
m = euler_phi

try:
    res=find_mod_inv(a,m)
    print("The required modular inverse is: "+ str(res))

except:
    print('The modular inverse does not exist.')    
    
modular_inverse = find_mod_inv(a,m)


message = int(input("Message to encrypt: "))


#encrypt message
message_encrypt = (message**get_co_prime)%(n_modulus)


print("Message Encypt: " + str(message_encrypt))


decrypted_message = (message_encrypt**modular_inverse)%(n_modulus)



print("Message Descrypted: " + str(decrypted_message))

