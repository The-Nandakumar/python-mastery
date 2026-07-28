# List

# List is used to store multiple items in a single variable.
# List is one of 4 built-in data types in python.
# A Python list is a sequence of comma separated items, enclosed in square brackets []. 

listitems = ["apple", 24, 65.4, True]
print(listitems)

# It can contain different data types like string, integer, float, etc.
# List items are ordered, changeable and allow duplicate values.

# Accessing list items
# List items are indexed and you can access them by referring to the index number.
print(listitems[0])
print(listitems[1])
print(listitems[2])
print(listitems[3])

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(listitems[-1])
print(listitems[-2])

# Range of indexes (After : the number represents the end index, but the end index is not included)
print(listitems[1:3])
# Output [24, 65.4]

print(listitems[:3])
# Output ['apple', 24, 65.4]

print(listitems[2:])
# Output [65.4, True]

# Negative index
print(listitems[-3:-1])
# Output [24, 65.4]

# You can also change the value of a specific item by referring to its index number.
listitems[1] = "banana"
print(listitems)
# Output ['apple', 'banana', 65.4, True]


# List length

# To determine length of a list we can use the len() function.
print(len(listitems))

# List constructor

# It is also possible to use the list() constructor to make a list.
newlist = list(("apple", "banana", "cherry"))
print(newlist)

# From python perspective list is object with the data type 'list'.
print(type(newlist))


# List methods

# 1. append() - Adds an element at the end of the list
newlist.append("orange")
print(newlist)

# 2. insert() - Adds an element at the specified position
newlist.insert(1, "kiwi")
print(newlist)

# 3. remove() - Removes the first item with the specified value
newlist.remove("banana")
print(newlist)

# 4. pop() - Removes the element at the specified position
newlist.pop(3)
print(newlist)

# 5. index() - Returns the index of the first element with the specified value
print(newlist.index("cherry"))

# 6. count() - Returns the number of elements with the specified value
newlist.insert(1, "apple")
print(newlist.count("apple"))

# 7. sort() - Sorts the list
newlist.sort()
print(newlist)

# 8. reverse() - Reverses the order of the list
newlist.reverse()
print(newlist)

# 9. copy() - Returns a copy of the list
newlist2 = newlist.copy()
print(newlist2)

# 10. extend() - Add the elements of a list (or any iterable), to the end of the current list
newlist.extend(["grape", "melon"])
newlist.extend(("kiwi", "mango"))
print(newlist)

# 11. clear() - Removes all the elements from the list
newlist.clear()
print(newlist)

# 12. del() - Removes the specified index
del newlist2[2]
print(newlist2)

# 13. del() - Removes the entire list
del newlist2
# print(newlist2)  # This will raise an error because newlist2 has been deleted

# List functions
# 1. len() - Returns the number of items in a list
print(len(newlist))

# 2. max() - Returns the largest item in a list
numbers = [1, 2, 3, 4, 5]
print(max(numbers))

# 3. min() - Returns the smallest item in a list
print(min(numbers))

# 4. sum() - Returns the sum of all items in a list
print(sum(numbers))

# 5. sorted() - Returns a new sorted list from the items in an iterable
unsorted_list = [3, 1, 4, 2]
print(sorted(unsorted_list))

# 6. reversed() - Returns a reversed iterator of the list
print(list(reversed(unsorted_list)))

# 7. any() - Returns True if any item in the list is True
bool_list = [False, False, True]
print(any(bool_list))

# 8. all() - Returns True if all items in the list are True
bool_list2 = [True, True, True]
print(all(bool_list2))

# 9. enumerate() - Returns an enumerate object, which contains the index and value of each item in the list
enum_list = ["apple", "banana", "cherry"]
for index, value in enumerate(enum_list):
    print(index, value)

# 10. zip() - Returns an iterator of tuples, where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together, etc.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))

# 11. list() - Converts an iterable (like a tuple or string) into a list
tuple_items = (1, 2, 3)
print(list(tuple_items))
string_items = "hello"
print(list(string_items))