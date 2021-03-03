def naive_search(l, target) :
    
    if target in l :
        return(l.index(target))
    else :
        return(-1)

l1_input = input('Enter your list of numbers')
l1 = []
for num in l1_input :
    if num == ' ':
        continue
    else :
        l1.append(int(num))

t1 = int(input('Enter your target number'))

print(l1)
print(t1)
print(naive_search(l1, t1))



