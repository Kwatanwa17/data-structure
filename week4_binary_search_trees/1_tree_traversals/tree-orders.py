# python3

import sys, threading, fileinput

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):

        # self.n = int(sys.stdin.readline())

        f = open("./tests/2")
        self.n = int(f.readline())

        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            # [a, b, c] = map(int, sys.stdin.readline().split())
            [a, b, c] = map(int, f.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        current = 0
        # stack
        s = [current]

        while s:

            # if the vertex has a left son
            if self.left[current] != -1:
                # append the left son index to the stack
                s.append(self.left[current])
                current = self.left[current]
                # if self.left[current] == -1 the stack remains as it is
                continue
            if current != -1:
                self.result.append(self.key[current])
            s.pop()

            # current belongs to the left subtree of the last element of the stack, which is its ancestor
            while s and (self.left[s[len(s) - 1]]) != current:
                current = s[len(s) - 1]
                if current != -1:
                    self.result.append(self.key[current])
                s.pop()

            if s:
                s.append(self.right[current])
                current = self.right[current]
                # if current != -1:
                #     self.result.append(self.key[current])
            # go to the right subtree
            elif len(self.result) < len(self.key):
                s.append(self.right[current])
                current = self.right[current]

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        current = 0
        # stack
        s = [current]

        while s:
            if self.key[current] not in self.result and current != -1:
                self.result.append(self.key[current])

            # if the vertex has a left son
            if self.left[current] != -1:
                # append the left son index to the stack
                s.append(self.left[current])
                current = self.left[current]
                # if self.left[current] == -1 the stack remains as it is
                continue

            s.pop()

            # current belongs to the left subtree of the last element of the stack, which is its ancestor
            while s and (self.left[s[len(s) - 1]]) != current:
                current = s[len(s) - 1]
                # if current != -1:
                #     self.result.append(self.key[current])
                s.pop()

            if s:
                s.append(self.right[current])
                current = self.right[current]
                # if current != -1:
                #     self.result.append(self.key[current])
            # go to the right subtree
            elif len(self.result) < len(self.key):
                s.append(self.right[current])
                current = self.right[current]

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        current = 0
        # stack
        s = [current]

        while s:

            # if the vertex has a left son
            if self.left[current] != -1:
                # append the left son index to the stack
                s.append(self.left[current])
                current = self.left[current]
                # if self.left[current] == -1 the stack remains as it is
                continue
            if self.left[current] == -1 and self.right[current] == -1:
                s.pop()

            if self.key[current] not in self.result and current != -1:
                self.result.append(self.key[current])

            # current belongs to the left subtree of the last element of the stack, which is its ancestor
            while s and (self.left[s[len(s) - 1]]) != current:
                current = s[len(s) - 1]
                # if current != -1:
                #     self.result.append(self.key[current])
                if self.left[current] == -1 and self.right[current] == -1:
                    s.pop()
                else:
                    break

            if s:
                if self.right[current] not in s:
                    if self.key[self.right[current]] not in self.result:
                        s.append(self.right[current])
                        current = self.right[current]
                # if current != -1:
                #     self.result.append(self.key[current])
            # go to the right subtree
            elif len(self.result) < len(self.key):
                s.append(self.right[current])
                current = self.right[current]


        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
