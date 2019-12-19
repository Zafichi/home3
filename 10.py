lst1 = [1, 2, 3, 5, 8, 13, 42, 5, 8]
lst2 = [5, 8, 13, 42]
new_lst = []
for i in lst1:
    if i in lst2:
        new_lst.append(i)

print(new_lst)
