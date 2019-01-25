#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):

    bribes = 0

    # Makes an iteration of the list until it is in order again (undoing all bribes to count them)
    while q != list(range(1, len(q) + 1)):

        for i, n in enumerate(q):

            #  If the position that is being analyzed is more than two positions far from his original or
            #  designated position in the queue it's automatically chaotic
            if n - (i + 1) > 2:
                print("Too chaotic")

                return

            try:

                # If the position that is being analyzed, it is bigger than the next position,
                # the position get inverted and the bribe counter get increased.
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
