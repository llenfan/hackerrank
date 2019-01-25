#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):

    bribes = 0

    while q != list(range(1, len(q) + 1)):

        for i, n in enumerate(q):

            if n - (i + 1) > 2:
                print("Too chaotic")

                return

            try:

                if q[i] > q[i + 1]:
                    q[i], q[i + 1] = q[i + 1], q[i]

                    bribes = bribes + 1

            except IndexError:
                pass
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
