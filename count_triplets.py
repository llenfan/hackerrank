#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):

    counter_arr = Counter(arr) # Forward frequency counting
    c = Counter()  # Backward frequency counting

    triplets = 0

    for i in arr:

        # Subtracting occurrences from one counter to another
        counter_arr.subtract([i])

        """
        Explanation: The counter of triplets make a sum when being focused and analzing i value, if it exists 
        in the previus value on his geometric projection (i / r) and whose aparition frecuency is getting loaded 
        on the backward counting (past values), and when also exists his next value on the geometric projection 
        (i * r) and  his frecuency on the forward counter (counter_arr).
        """

        triplets += c.get(i / r, 0) * counter_arr.get(i * r, 0)

        # Updating backward frequency counter with the element that the forward counter has removed.
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
