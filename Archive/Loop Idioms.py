largesr_so_far = -1 
print("Before", largesr_so_far)
for the_num in [9, 41, 12 , 3, 74, 15]:
    if the_num > largesr_so_far:
        largesr_so_far = the_num
    print(largesr_so_far, the_num)

print("After", largesr_so_far)