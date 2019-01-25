#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    case_is_valid = True
    # Initial validation
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        case_is_valid = False
    else:
        if re.search('[^a-z\,]', s):
            case_is_valid = False
        elif (len(s) > 10 ** 5 or len(s) < 1):
            case_is_valid = False

    if not case_is_valid:
        return "NO"

    # Getting frequency of each char
    char_freq = {}
    for ch in s:
        if ch in char_freq:
            char_freq[ch] = char_freq[ch] + 1
        else:
            char_freq[ch] = 1

    # Grouping the frequencies
    highest_freq = 0
    char_freq_group = {}
    for key, value in char_freq.items():
        if value in char_freq_group:
            char_freq_group[value] = char_freq_group[value] + 1
        else:
            char_freq_group[value] = 1

        # If in any moment exist more than 2 frequencies that implies NO
        if len(char_freq_group) > 2:
            case_is_valid = False
            break

        # Higher frequency found
        if value != 1 and value > highest_freq:
            highest_freq = value

        discardable_freq = False
        if 1 in char_freq_group:
            if char_freq_group[1] == 1:
                # If there is a frequency with just one char/repetition can be discarded
                discardable_freq = True

        equalizable_freq = False
        if highest_freq > 0:
            if len(char_freq_group) == 2:
                # lower freq detected
                if (highest_freq - 1) in char_freq_group:
                    # If there is a frequency  that can be equalized by deleting one char
                    if char_freq_group[highest_freq] == 1:
                        equalizable_freq = True

    # If there is just two frequencies but neither of them are discardable or equalizable then the case is not valid
    if len(char_freq_group) == 2:
        if not (discardable_freq or equalizable_freq):
            case_is_valid = False

    if case_is_valid:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')
    
    fptr.close()