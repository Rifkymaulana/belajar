fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# 1. list.count(x) => Return the number of times x appears in the list.
orange = fruits.count('apple')
print(orange)

# 2.  list.index(x[, start[, end]]) => Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
indexOfBanana = fruits.index('banana')
indexOfBananaOptional = fruits.index('banana', 4)
print(indexOfBanana)
print(indexOfBananaOptional)

# 3. list.reverse() => Reverse the elements of the list in place.
fruits.reverse()
print(fruits)

# 4. list.append(x) => Add an item to the end of the list. Equivalent to a[len(a):] = [x].
fruits.append('grape')
print(fruits)

# 5. list.sort(*, key=None, reverse=False) => Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
fruits.sort()
print(fruits)

# 6.  list.pop(i) => Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
fruits.pop(5)
print(fruits)

print(1)

