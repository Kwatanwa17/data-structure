#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # set exit value
    exit_value = True
    if len(tree) > 0:

        # key
        key = [i[0] for i in tree]

        # left
        left = [i[1] for i in tree]

        # right
        right = [i[2] for i in tree]

        current = 0
        result = []
        result_idx = []

        # stack
        s = []

        # set exit value
        exit_value = True

        # subtree 0 = left, 1 = right
        # subtree = 0

        while exit_value:
            if current != -1:
                s.append(current)
                current = left[current]

            elif s:
                current = s.pop()

                # check current node sons
                if left[current] != -1:
                    if key[left[current]] < key[current]:
                        pass
                    else:
                        exit_value = False

                if right[current] != -1:
                    if key[right[current]] >= key[current]:
                        pass
                    else:
                        exit_value = False

                result.append(key[current])

                current = right[current]

            else:
                break

        # find index of the root node
        # root_idx = result_idx.index(0)

        if sorted(result) != result:
            exit_value = False

    return exit_value


def main():
    # f = open("./tests/4")
    # nodes = int(f.readline().strip())
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
        # tree.append(list(map(int, f.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
