import time
from fibonacci import FibonacciHeap
from leftist import Leftist
from twothreeheap import TwoThreeMinHeap

def run_with_stats(heap_class, file_path):
    heaps = {}

    with open(file_path) as f:
        n = int(f.readline())
        start = time.perf_counter()

        for _ in range(n):
            parts = list(map(int, f.readline().split()))
            if not parts:
                continue

            op = parts[0]
            if op == 1:
                _, x, y = parts
                if x not in heaps:
                    heaps[x] = heap_class()
                heaps[x].insert(y)

            elif op == 2:
                _, x, y = parts
                if x not in heaps:
                    heaps[x] = heap_class()
                if y in heaps:
                    heaps[x].merge(heaps[y])
                    heaps[y] = heap_class()  

            elif op == 3:
                _, x = parts
                if x in heaps:
                    result = heaps[x].extract_min()

        end = time.perf_counter()
    
    return end - start, n

heaps = {
    "Fibonacci": FibonacciHeap,
    "Leftist": Leftist,
    "2-3": TwoThreeMinHeap
}

tests = [
    "tests/insert_heavy.in",
    "tests/merge_heavy.in",
    "tests/extract_heavy.in",
    "tests/balanced.in"
]

for heap_name, heap_class in heaps.items():
    print(f"\n==== Teste pentru {heap_name} Heap ====")
    for test_file in tests:
        try:
            runtime, total = run_with_stats(heap_class, test_file)
            print(f">> {test_file:<30} | timp: {runtime:.4f}s | operații: {total}")
        except Exception as e:
            print(f">> {test_file:<30} | EROARE: {str(e)}")
