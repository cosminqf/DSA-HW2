class Nod:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.npl = 0 #null path length

class Leftist:
    def __init__(self):
        self.rad = None

    def merge(self, other):
        self.rad = self.merge1(self.rad, other.rad)

    def merge1(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        
        if h1.val > h2.val:
            h1, h2 = h2, h1
        
        h1.right = self.merge1(h1.right, h2)

        if h1.left is None:
            st_npl = -1
        else:
            st_npl = h1.left.npl
        if h1.right is None:
            dr_npl = -1
        else:
            dr_npl = h1.right.npl
        
        if st_npl < dr_npl:
            h1.left, h1.right = h1.right, h1.left
        
        h1.npl = 1 + min(st_npl, dr_npl)

        return h1
    
    def insert(self, val):
        nod = Nod(val)
        self.rad = self.merge1(self.rad, nod)
    
    def extract_min(self):
        if self.rad is None:
            return "Heap-ul nu are radacina"
        mn = self.rad.val
        self.rad = self.merge1(self.rad.left, self.rad.right)
        return mn

"""
heap = Leftist()
heap2 = Leftist()
heap.insert(5)
heap.insert(10)
heap.insert(100)
heap.insert(23)
heap.insert(2)
heap2.insert(25)
heap2.insert(233)
heap2.insert(1)

print(heap.extract_min())
print(heap.extract_min())
heap.merge(heap2)
print(heap.extract_min())
"""
