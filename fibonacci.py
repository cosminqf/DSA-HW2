import math

class FibonacciNode:
    __slots__ = ("key", "grad", "mark", "parinte", "copil", "left", "right")

    def __init__(self, key):
        self.key = key
        self.grad = 0
        self.mark = False
        self.parinte = None
        self.copil = None
        self.left = self
        self.right = self

class FibonacciHeap:
    __slots__ = ("min", "n")

    def __init__(self):
        self.min = None
        self.n = 0

    def insert(self, key):
        node = FibonacciNode(key)
        if self.min is None:
            self.min = node
        else:
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node
            if node.key < self.min.key:
                self.min = node
        self.n += 1
        return node

    def merge(self, other: 'FibonacciHeap'):
        if other.min is None:
            return
        if self.min is None:
            self.min = other.min
            self.n = other.n
        else:
            a = self.min.right
            b = other.min.left
            self.min.right = other.min
            other.min.left = self.min
            a.left = b
            b.right = a
            if other.min.key < self.min.key:
                self.min = other.min
            self.n += other.n
        other.min = None
        other.n = 0

    def extract_min(self):
        z = self.min
        if z is not None:
            if z.copil is not None:
                copii = []
                c = z.copil
                while True:
                    copii.append(c)
                    c = c.right
                    if c is z.copil:
                        break
                for x in copii:
                    x.left.right = x.right
                    x.right.left = x.left
                    x.left = self.min
                    x.right = self.min.right
                    self.min.right.left = x
                    self.min.right = x
                    x.parinte = None
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()
            self.n -= 1
        return z.key if z else None

    def _consolidate(self):
        max_deg = int(math.log2(self.n)) + 2
        A = [None] * max_deg
        nodes = []
        w = self.min
        if w:
            nodes.append(w)
            w = w.right
            while w is not self.min:
                nodes.append(w)
                w = w.right
        for w in nodes:
            x = w
            d = x.grad
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = None
        for node in A:
            if node is not None:
                node.left = node.right = node
                if self.min is None:
                    self.min = node
                else:
                    node.left = self.min
                    node.right = self.min.right
                    self.min.right.left = node
                    self.min.right = node
                    if node.key < self.min.key:
                        self.min = node

    def _link(self, y: FibonacciNode, x: FibonacciNode):
        y.left.right = y.right
        y.right.left = y.left
        y.parinte = x
        if x.copil is None:
            x.copil = y
            y.left = y.right = y
        else:
            y.left = x.copil
            y.right = x.copil.right
            x.copil.right.left = y
            x.copil.right = y
        x.grad += 1
        y.mark = False
