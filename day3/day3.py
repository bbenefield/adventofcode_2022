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

elf_groups = np.array_split(rucksacks, 3)

print(1)