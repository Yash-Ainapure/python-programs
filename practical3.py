# list
lst=[1,5,7,3]
print("list at 1st stage")
print(lst)
print()


# access list variables
print("accessing 2 index item")
print(lst[2])
print()

# change list elements
print("change 1 index item to 98")
lst[1]=98
print(lst)
print()

# add/append new items to list
print("appending new element")
lst.append(101)
print(lst)
print()


# remove list items
print("removing element 1")
lst.remove(1)
print(lst)
print()


# print list items
print("printing list elements")
for element in lst:
   print(element)


# sort list
print("sorting list in ascending order")
lst.sort()
# in reverse order
# lst.sort(reverse=True)
# lst.reverse
print(lst)
print()


# copying list items to another list
lst2=lst.copy()
# lst2=lst[1:3]
print("copied list:")
print(lst2)
print()


# joining 2 lists together
lst3=lst+lst2
print("2 joined list")
print(lst3)


# appending a list to another one
lst4=lst.extend(lst2)