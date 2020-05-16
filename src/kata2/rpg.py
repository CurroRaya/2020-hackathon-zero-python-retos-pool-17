#!/usr/bin/python

import random
import string

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

def RandomPasswordGenerator(passLen=10):
    password = ''

    for p in range(passLen):
        password += random.choice(chars)

    print (password)
