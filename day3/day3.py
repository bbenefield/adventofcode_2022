import string

import numpy as np

alphabet_map = dict(zip(list(string.ascii_letters), list(range(1,53))))

with open('day3/day3_input.txt', 'r') as fin:
    rucksacks = fin.readlines()

# total_count = 0
   
# for rucksack in rucksacks:
#     contents = list(rucksack.strip())
#     split_loc = len(contents)//2
    
#     total_count += alphabet_map[(set(contents[:split_loc]) & set(contents[split_loc:])).pop()]
    
# print(total_count)

elf_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

total_points = 0
for elf in elf_groups:
    total_points += alphabet_map[(set(elf[0].strip()) & set(elf[1].strip()) & set(elf[2].strip())).pop()]
    
print(total_points)