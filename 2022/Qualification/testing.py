

rows, cols = 2, 2

def generate_trees(rows, cols):
    return "\n".join(["^" * cols] * rows)

print(generate_trees(rows, cols))