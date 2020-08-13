# python3

import sys, threading, fileinput

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):

        self.n = int(sys.stdin.readline())

        # f = open("./tests/2")
        # self.n = int(f.readline())

        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            # [a, b, c] = map(int, f.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        current = 0
        # stack
        s = []

        while True:

            if current != -1:
                s.append(current)
                current = self.left[current]

            elif s:
                current = s.pop()
                self.result.append(self.key[current])

                current = self.right[current]

            else:
                break

        return self.result

    def preOrder(self):
        self.result = []

        current = 0
        s = []

        # push root to the stack
        s.append(current)

        while s:

            # pop the top element of the stack and set it as current
            current = s.pop()
            self.result.append(self.key[current])

            # push left and right sons to the stack
            if self.right[current] != -1:
                s.append(self.right[current])

            if self.left[current] != -1:
                s.append(self.left[current])

        return self.result

    def postOrder(self):
        # create an empty stack
        self.result = []

        current = 0

        # use 2 stacks
        s1 = []
        s2 = []

        # push current to the stack 1
        s1.append(current)

        while s1:
            current = s1.pop()
            s2.append(current)

            if self.left[current] != -1:
                s1.append(self.left[current])

            if self.right[current] != -1:
                s1.append(self.right[current])

        # map index to key
        for idx in reversed(s2):
            self.result.append(self.key[idx])

        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
