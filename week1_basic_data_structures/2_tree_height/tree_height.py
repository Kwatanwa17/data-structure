# python3

import sys
import threading


def compute_height(n, parents):
    # parents
    if not isinstance(parents, list):
        parents = parents.split(' ')

    # initialize a tree dictionary
    tree = {}
    for i in range(n):
        tree[str(i)] = []

    # loop over the parents array
    for idx, p in enumerate(parents):
        if str(p) == '-1':
            root = str(idx)
        else:
            tree[str(p)].append(str(idx))

    # BFS
    stack = [root]
    children = []
    levels = [1]

    while len(stack) > 0:

        # get children
        for parent in stack:
            children += tree[parent]

        # if leaf
        if len(children) < 1:
            break

        # assign children to stack
        levels.append(len(children))
        stack = children
        children = []

    return len(levels)


def main():
    # comment out for test
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

    # import os
    #
    # filename_list = []
    #
    # for root, dirs, files in os.walk("./tests"):
    #
    #     for filename in files:
    #         if '.a' not in filename:
    #             filename_list.append(filename)
    #             filename_list.sort()
    #
    #     for filename in filename_list:
    #         print('........................')
    #         print('Running Test: ' + filename)
    #         f = open("./tests/" + filename, "r")
    #
    #         if f.mode == 'r':
    #             lines = f.readlines()
    #             n = lines[0].strip()
    #             parents = lines[1].strip()
    #             f.close()
    #             f = open("./tests/" + filename + '.a', "r")
    #
    #         if f.mode == 'r':
    #             expected_output = f.read().rstrip('\n')
    #             f.close()
    #
    #         output = compute_height(int(n), parents)
    #
    #         print('Inputs: ')
    #         print('n: ' + str(n))
    #         print('parents: ' + str(parents))
    #         print('Expected Output: ' + str(expected_output))
    #         print('Ouput: ' + str(output))
    #
    #     if str(expected_output) == str(output):
    #         print('Test Passed')
    #     else:
    #         print('Test Failed')
    #         break


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
