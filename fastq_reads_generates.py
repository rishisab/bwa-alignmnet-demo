import random

ref = "ATGCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA"

def mutate_one(seq, pos):
    bases = ["A","T","G","C"]
    bases.remove(seq[pos])
    return seq[:pos] + random.choice(bases) + seq[pos+1:]

read = ref[:30]

start = mutate_one(read, 1)     # safe mutation
middle = mutate_one(read, 15)
end = mutate_one(read, 28)

with open("reads2.fastq", "w") as f:
    for name, seq in [("start", start), ("middle", middle), ("end", end)]:
        f.write(f"@{name}\n{seq}\n+\n{'I'*len(seq)}\n")
