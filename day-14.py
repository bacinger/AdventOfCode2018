input = 894501

elf_1 = 0
elf_2 = 1
score = 10
recipes = [3, 7]
while len(recipes) < input + score:
    for ch in str(recipes[elf_1] + recipes[elf_2]):
        recipes.append(int(ch))
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)
print('Part 1:', ''.join(str(e) for e in recipes)[input:input + score])

# Warning: This naive solution for Part 2 is extremely slow and inefficient!
elf_1 = 0
elf_2 = 1
recipes = [3, 7]
ic = [int(c) for c in str(input)]
while recipes[-len(ic):] != ic:
    for ch in str(recipes[elf_1] + recipes[elf_2]):
        recipes.append(int(ch))
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)
print('Part 2:', (len(recipes) - len(ic)))