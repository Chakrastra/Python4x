#List comprehention and set oprations

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

union= set1.union(set2)
intersection= set1.intersection(set2)
difference= set1.difference(set2)

union_squares = [n**2 for n in union]

print("Union set:", union)
print("Intersection set:", intersection)
print("Difference set:", difference)
print("Square of Union set:", union_squares)