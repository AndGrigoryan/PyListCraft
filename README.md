# CraftedList

CraftedList is a custom Python class that replicates the functionality of built-in lists, including additional methods for custom list manipulation.

## Features

- **Custom Implementation:** CraftedList provides a custom implementation of common list methods.
- **Usage:** Easily use methods like append, pop, index, len, and more.
- **Sort Method:** Now includes a custom implementation of the `sort` method, allowing sorting based on a custom key function and supporting reverse sorting.
- **Additional Methods:**
  - `clear`: Remove all elements from the list.
  - `copy`: Create a shallow copy of the list.
  - `count`: Count occurrences of a specific element.
  - `extend`: Extend the list by appending elements from an iterable.
  - `index`: Return the index of the first occurrence of a specific element.
  - `insert`: Insert an element at a given position.
  - `pop`: Remove and return the last element or an element at a specific position.
  - `remove`: Remove the first occurrence of a specific element.
  - `reverse`: Reverse the elements of the list in place.
  - `sort`: Sort the elements of the list in ascending or descending order based on a custom key function.

## Example

```python
# Create a CraftedList instance
my_list = CraftedList("aaa", "bbbb", "aaaaa", "bb", "b", "aaaaaa")
print(my_list)

# Use list methods
my_list.sort(key=len, reverse=True)
print(my_list)  # Output: CraftedList: ['aaaaaa', 'aaaaa', 'bbbb', 'aaa', 'bb', 'b']

# Use additional methods
my_list.extend(["new", "elements"])
print(my_list)  # Output: CraftedList: ['aaaaaa', 'aaaaa', 'bbbb', 'aaa', 'bb', 'b', 'new', 'elements']
