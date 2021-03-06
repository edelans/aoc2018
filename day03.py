#!/usr/bin/env python3
"""Template file to be used as boilerplate for each day puzzle."""
from aoc_utilities import Input
import aocd
import sys
# import itertools
import re


# day must be 2 digit
DAY = '03'


"""
PART1
"""


def solve1(input):
    """Solves part 1."""

    # must parse "#id @ x,y: widthxheight" as in following example :
    # 1 @ 1,3: 4x4
    regex = r"^#(?P<id>\d+)\s@\s(?P<x>\d+),(?P<y>\d+):\s(?P<width>\d+)x(?P<height>\d+)"

    # Store the mapping in a dict. Key is coordinates (tuple), value is a list of ID claims.
    mapping = {}

    for claim in input:
        matches = re.search(regex, claim)
        if matches:
            id = matches.group('id')
            x, y = int(matches.group('x')), int(matches.group('y'))
            width, height = int(matches.group('width')), int(matches.group('height'))
            for i in range(x, x + width):
                for j in range(y, y + height):
                    mapping[(i, j)] = mapping.get((i, j), []) + [id]
    # count overlaps :
    return len([k for k in mapping.values() if len(k) >= 2])


"""
PART 2
"""


def solve2(input):
    """Solves part2."""

    # must parse "#id @ x,y: widthxheight" as in following example :
    # 1 @ 1,3: 4x4
    regex = r"^#(?P<id>\d+)\s@\s(?P<x>\d+),(?P<y>\d+):\s(?P<width>\d+)x(?P<height>\d+)"

    # Store the mapping in a dict. Key is coordinates (tuple), value is a list of ID claims.
    mapping = {}

    # store claim ids in a set so we can purge him from overlaping ids later
    id_set = set([])

    for claim in input:
        matches = re.search(regex, claim)
        if matches:
            id = matches.group('id')
            x, y = int(matches.group('x')), int(matches.group('y'))
            width, height = int(matches.group('width')), int(matches.group('height'))
            id_set.add(id)
            for i in range(x, x + width):
                for j in range(y, y + height):
                    mapping[(i, j)] = mapping.get((i, j), []) + [id]


    # part 2 really starts here

    overlaping_ids = set([l for k in mapping.values() if len(k) >= 2 for l in k])

    # Tip : remember that nested comprehension list follow the same order of the corresponding for loop
    # see https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/
    # for k in mapping.values():
    #     if len(k) >= 2:
    #         for l in k:
    #             l

    for overlap_id in overlaping_ids:
        id_set.discard(overlap_id)

    return id_set.pop()


"""
Use script args to execute the right function.
"""
if __name__ == '__main__':
    if sys.argv[1] == '1':
        res = solve1((Input(DAY).readlines()))
        print(res)
        if len(sys.argv) == 3:
            if sys.argv[2] == 's':
                print("attempting to submit the response '{}' to part 1: \n\n".format(res))
                aocd.submit1(res)

    if sys.argv[1] == '2':
        res = solve2((Input(DAY).readlines()))
        print(res)
        if len(sys.argv) == 3:
            if sys.argv[2] == 's':
                print("attempting to submit the response '{}' to part 2: \n\n".format(res))
                aocd.submit2(res)
