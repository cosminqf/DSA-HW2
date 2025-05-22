import random

def save_test(filename, ops):
    with open(f"tests/{filename}", "w") as f:
        f.write(f"{len(ops)}\n")
        for op in ops:
            f.write(" ".join(map(str, op)) + "\n")
    print(f"Test salvat: tests/{filename}")

def generate_insert_heavy(filename, ops=1000, heaps=5, max_val=1000):
    operations = []
    for _ in range(ops):
        h = random.randint(1, heaps)
        val = random.randint(1, max_val)
        operations.append((1, h, val))  
        if random.random() < 0.05:  
            operations.append((3, h))  
    save_test(filename, operations)

def generate_merge_heavy(filename, ops=1000, heaps=10, max_val=1000):
    operations = []
    for _ in range(ops):
        choice = random.random()
        if choice < 0.5:
            h1, h2 = random.sample(range(1, heaps + 1), 2)
            operations.append((2, h1, h2))  
        else:
            h = random.randint(1, heaps)
            val = random.randint(1, max_val)
            operations.append((1, h, val))  
    save_test(filename, operations)

def generate_extract_heavy(filename, ops=1000, heaps=5, max_val=1000):
    operations = []
    for _ in range(ops):
        h = random.randint(1, heaps)
        val = random.randint(1, max_val)
        operations.append((1, h, val))  
    for _ in range(ops // 2):  
        h = random.randint(1, heaps)
        operations.append((3, h))  
    save_test(filename, operations)

def generate_balanced(filename, ops=1000, heaps=5, max_val=1000000):
    operations = []
    for _ in range(ops):
        op = random.choices([1, 2, 3], weights=[40, 30, 30])[0]
        if op == 1:
            h = random.randint(1, heaps)
            val = random.randint(1, max_val)
            operations.append((1, h, val))  
        elif op == 2:
            h1, h2 = random.sample(range(1, heaps + 1), 2)
            operations.append((2, h1, h2))  
        elif op == 3:
            h = random.randint(1, heaps)
            operations.append((3, h)) 
    save_test(filename, operations)

if __name__ == "__main__":
    generate_insert_heavy("insert_heavy.in", ops=1000000)
    generate_merge_heavy("merge_heavy.in", ops=1000000)
    generate_extract_heavy("extract_heavy.in", ops=1000000)
    generate_balanced("balanced.in", ops=1000000)
