#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):
    counter_arr = Counter(arr)

    c = Counter()

    triplets = 0

    for i in arr:
        counter_arr.subtract([i])

        triplets += c.get(i / r, 0) * counter_arr.get(i * r, 0)
        c.update([i])

    return triplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
