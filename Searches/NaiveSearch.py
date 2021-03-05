import time

# iterate through a list and find location of a target item

def naive_search(l, t) :
    
    if t in l :
        return(l.index(t))
    else :
        return(-1)

# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/ get a list from
# user inputs 

# also make sure user enters valid numbers
is_valid = False
while is_valid == False:
    try :
        lst = list(map(int,input("\nEnter your numbers : ").strip().split()))
        is_valid = True
    except :
        print('Please enter valid numbers seperated be a space')
        continue


target = int(input('\nEnter your target number: '))

print(f'\nYour List: {lst}')
print(f'\nYour Target: {target}')
# if a number is in list more than once, print number of times and all indexes

# track number of duplicates
target_count = 0
for num in lst :
    if num == target :
        target_count += 1

# track duplicate indexes, add them to a list to be printed
dupl_index_list = []
for index, dup in enumerate(lst):
        if dup == target :
            dupl_index_list.append(index)

if target_count > 1 :
    print(f'\nYour Target appeared {target_count} times in the list at indexes {dupl_index_list}\n')
else :
    print(f'\nIndex of Target in List: {naive_search(lst, target)} \n(-1 = target not in list)\n')
