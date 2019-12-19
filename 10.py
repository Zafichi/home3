lst1 = [1, 2, 3, 5, 8, 13, 42, 5, 8]
lst2 = [5, 8, 13, 42]

new_lst = []
for i in lst1:
    if i in lst2:
        for j in lst2:
            new_lst.append(j)
    if len(new_lst) == len(lst2):
        break

if new_lst == lst2:
    print('True')
else:
    print('False')
print(new_lst)
print(len(lst2))
