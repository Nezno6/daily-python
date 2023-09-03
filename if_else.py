#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(n):
    if n%2 != 0 or 6<=n<=20:
        return "Weird"
    return "Not Weird"

if __name__ == '__main__':
    for i in range(1,101):
        print(i,is_weird(i))
