# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self._max_depth = 0
                self._depth = [0] * self.n

        def compute_height(self):
                # Replace this code with a faster implementation
                if self._max_depth is 0:
                        for idx,parent in enumerate(self.parent):
                                depth = self.get_depth(idx)
                                if self._max_depth < depth:
                                        self._max_depth = depth
                return self._max_depth

        def get_depth(self,idx):
                depth = self._depth[idx]
                if depth != 0:
                        return depth
                parent = self.parent[idx]
                if parent == -1:
                        depth = 1
                else:
                        depth = self.get_depth(parent) + 1

                self._depth[idx] = depth

                return depth

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
