#!/usr/bin/env python3
import os
from insecure_hash import hash_string
#from Cryptodome.Cipher import AES
import math
from Cryptodome.Cipher import AES


def find_collision(original_message): 
    # find the hash 
    hashed_msg = hash_string(original_message) 
    # use abitrary key with 16 byte 
    cipher = AES.new(b'VVVVWWWWXXXXYYYY', mode=AES.MODE_ECB) 
    unhashed = cipher.encrypt(hashed_msg) # encrypts ("dehashes") the message with arbitrary key
    # returns the collision 
    return unhashed + b'VVVVWWWWXXXXYYYY' 


if __name__ == '__main__':
    message = b"aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb"
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
