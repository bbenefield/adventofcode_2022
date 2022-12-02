from collections import defaultdict

with open('day1/day1_input.txt', 'r') as fin:
    calorie_count = fin.readlines()

elf_inventory = defaultdict(int)
elf_number = 1

for line in calorie_count:
    calorie = line.strip()
    if not calorie:
        elf_number += 1
    else:
        elf_inventory[f'elf_{elf_number}'] += int(calorie)
        
print(sum(list(sorted(elf_inventory.values(), key=lambda item: item))[-3:]))