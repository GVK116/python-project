#!/bin/python3

import math
# import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    a.reverse()
    return a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())

    arr_count = 4

    arr = list(map(int, input().split()))

    res = reverseArray(arr)

    v = ' '.join(map(str, res))
    print(v)


