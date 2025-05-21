class nodFibonacci:
    def __init__(self, key):
        self.key = key
        self.grad = 0
        self.mark = False
        self.copil = None
        self.parinte = None
        self.st = self
        self.dr = self


class heapFibonacci:
    def __init__(self):
        self.nod_min = None
        self.noduri_totale = 0
    
    def insert(self, key):
        nod = nodFibonacci(key)
        self.nod_min = self.merge_lists(self.nod_min, nod)
        self.noduri_totale += 1
    
    def merge(self, other):
        if other and isinstance(other, heapFibonacci) and other.nod_min:
            self.nod_min = self.merge_lists(self.nod_min, other.nod_min)
            self.noduri_totale += other.noduri_totale



    def extract_min(self):
        x = self.nod_min
        if x:
            if x.copil:
                copii = [i for i in self.iterate(x.copil)]
                for copil in copii:
                    self.remove_list(copil)
                    self.nod_min = self.merge_lists(self.nod_min, copil)
                    copil.parinte = None
            
            self.remove_list(x)
            if x == x.dr:
                self.nod_min = None
            else:
                self.nod_min = x.dr
                self.cons()
            self.noduri_totale -= 1
            return x.key
        return None
    
    def cons(self):
        A = [None] * (self.noduri_totale + 1)
        root = [x for x in self.iterate(self.nod_min)]
        for c in root:
            x = c
            g = x.grad
            while A[g]:
                y = A[g]
                if y.key < x.key:
                    x, y = y,x
                self.link(y,x)
                A[g] = None
                g += 1
            A[g] = x
        self.nod_min = None
        for i in range(len(A)):
            if A[i]:
                self.nod_min = self.merge_lists(self.nod_min, A[i])

    def remove_list(self, nod):
        nod.st.dr = nod.dr
        nod.dr.st = nod.st

    def link(self, y, x):
        self.remove_list(y)
        y.st = y.dr= y
        x.copil = self.merge_lists(x.copil, y)
        y.parinte = x
        y.mark = False
        x.grad += 1

    def merge_lists(self, a, b):
        if not a:
            return b
        if not b:
            return a
        a.dr.st = b.st
        b.st.dr = a.dr
        a.dr = b
        b.st = a
        return a if a.key < b.key else b
    
    def iterate(self, head):
        nod = stop = head
        back = False
        while True:
            if nod == stop and back:
                break
            elif nod == stop:
                back = True
            yield nod
            nod = nod.dr