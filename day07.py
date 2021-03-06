#!/usr/bin/env python3
"""Template file to be used as boilerplate for each day puzzle."""
from aoc_utilities import Input
import aocd
import os
import sys
# import itertools

# 2 digit day fetched from filename
DAY = os.path.basename(__file__)[3:5]


"""
PART1
"""


def solve1(input):
    """Solves part 1."""
    requirements = {}  # if steps 3 requires steps 1 and 2 : {3 : [1, 2]}
    # build requirements mapping
    for line in input:
        req, st = line.split(' ')[1], line.split(' ')[7]
        requirements[st] = requirements.get(st, []) + [req]
        requirements[req] = requirements.get(req, [])
    print(requirements)

    # solve requirements one at a time
    res = ''
    while requirements != {}:
        for i in sorted(requirements.keys()):
            if requirements.get(i, []) == []:
                res += i
                if i in requirements:
                    del requirements[i]
                for j in requirements:
                    if i in requirements[j]:
                        requirements[j].remove(i)
                break  # because requirement simplification may have altered order sorted(requirements.key())
    return res


"""
PART 2
"""


def solve2(input):
    """Solves part2."""
    requirements = {}  # if steps 3 requires steps 1 and 2 : {3 : [1, 2]}
    # build requirements mapping
    for line in input:
        req, st = line.split(' ')[1], line.split(' ')[7]
        requirements[st] = requirements.get(st, []) + [req]
        requirements[req] = requirements.get(req, [])
    print(requirements)
    res = ''

    # init remaining time by step
    rem = {}
    k = 1
    for i in sorted(requirements.keys()):
        rem[i] = 60 + k
        k += 1

    # keep track of workers work
    workers = [''] * 5

    s = 0
    # iterate through each second
    while requirements != {}:
        for w in range(0, len(workers)):
            if workers[w] == '':
                # we have available workers: if there is a task requirements-free and not taken : assign worker !
                for i in [j for j in sorted(requirements.keys()) if j not in workers]:
                    if requirements[i] == []:
                        workers[w] = i
        for w in range(0, len(workers)):
            if workers[w] != '':
                # worker is busy, increment his work
                rem[workers[w]] -= 1
                if rem[workers[w]] == 0:
                    # a step has been competed !
                    for j in requirements:
                        if workers[w] in requirements[j]:
                            requirements[j].remove(workers[w])
                    del requirements[workers[w]]
                    res += workers[w]
                    workers[w] = ''

        s += 1

    print(res)
    return s

# 1860 too high
# 1859 too high
# My answer is 1120

"""
Use script args to execute the right function.
"""
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '1':
        res = solve1((Input(DAY).readlines()))
        print(res)
        if len(sys.argv) == 3:
            if sys.argv[2] == 's':
                print("attempting to submit the response '{}' to part 1: \n\n".format(res))
                aocd.submit1(res)

    if len(sys.argv) > 1 and sys.argv[1] == '2':
        res = solve2((Input(DAY).readlines()))
        print(res)
        if len(sys.argv) == 3:
            if sys.argv[2] == 's':
                print("attempting to submit the response '{}' to part 2: \n\n".format(res))
                aocd.submit2(res)
