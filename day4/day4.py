
with open('day4/day4_input.txt', 'r') as fin:
    pair_groups = fin.readlines()
    
pair_groups = [pair.strip().split(',') for pair in pair_groups]

overlap_count = 0

# for pair in pair_groups:
#     grid_0 = pair[0].split('-')
#     grid_1 = pair[1].split('-')
    
#     grid0_ids = [i for i in range(int(grid_0[0]), int(grid_0[1])+1)]
#     grid1_ids = [i for i in range(int(grid_1[0]), int(grid_1[1])+1)]
    
#     if set(grid0_ids).issubset(set(grid1_ids)) or set(grid1_ids).issubset(set(grid0_ids)):
#         overlap_count += 1
        
for pair in pair_groups:
    grid_0 = pair[0].split('-')
    grid_1 = pair[1].split('-')
    
    grid0_ids = set([i for i in range(int(grid_0[0]), int(grid_0[1])+1)])
    grid1_ids = set([i for i in range(int(grid_1[0]), int(grid_1[1])+1)])
    
    if not grid0_ids.isdisjoint(grid1_ids):
        overlap_count += 1
        
print(overlap_count)