#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = ''

    for p in range(passLen):
        password += random.choice(chars)

    return password
