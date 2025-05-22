class TwoThreeMinHeap:
    def __init__(self):
        self.heap = []
        
    def is_empty(self):
        return len(self.heap) == 0
    
    def insert(self, val):
        self.heap.append(val)
        self.sup(len(self.heap) - 1)
    
    def extract_min(self):
        if self.is_empty():
            return None
        
        min_val = self.heap[0]
        last_val = self.heap.pop()
        
        if not self.is_empty():
            self.heap[0] = last_val
            self.sdown(0)
            
        return min_val
    
    def merge(self, partner):
        for item in partner.heap:
            self.insert(item)
        partner.heap = []
    
    def sup(self, id):
        parent = (id - 1) // 2
        if id > 0 and self.heap[id] < self.heap[parent]:
            self.heap[id], self.heap[parent] = self.heap[parent], self.heap[id]
            self.sup(parent)
    
    def sdown(self, id):
        smallest = id
        L = 2 * id + 1
        R = 2 * id + 2
        
        if L < len(self.heap) and self.heap[L] < self.heap[smallest]:
            smallest = L
            
        if R < len(self.heap) and self.heap[R] < self.heap[smallest]:
            smallest = R
            
        if smallest != id:
            self.heap[id], self.heap[smallest] = self.heap[smallest], self.heap[id]
            self.sdown(smallest)

"""
TEST privat
if __name__ == "__main__":
    heap1 = TwoThreeMinHeap()
    heap2 = TwoThreeMinHeap()
    heap3 = TwoThreeMinHeap()

    heap2.insert(5)
    heap1.insert(3)
    heap3.insert(7)
    heap1.insert(4)
    heap2.insert(2)
    print(heap2.extract_min())
    heap2.merge(heap1)
    print(heap2.extract_min())
    heap3.merge(heap2)
    print(heap3.extract_min())
"""