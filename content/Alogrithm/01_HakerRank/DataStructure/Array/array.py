# https://www.hackerrank.com/challenges/arrays-ds/problem?h_r=profile
import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    reverse = []
    for i in range(arr_count-1, -1, -1):
        reverse.append(a[i])
    return reverse
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

