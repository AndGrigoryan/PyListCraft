# CraftedList

CraftedList is a custom Python class that replicates the functionality of built-in lists, excluding the `sort` method.

## Features

- **Custom Implementation:** CraftedList provides a custom implementation of common list methods.
- **Usage:** Easily use methods like append, pop, index, len, and more.
- **Sort Method:** Note that the sort method is not yet implemented.

## Example

```python
# Create a CraftedList instance
my_list = CraftedList(1, 3, 2, 4)

# Use list methods
my_list.append(5)
print(my_list)  # Output: CraftedList: [1, 3, 2, 4, 5]

# Note: Sort method is not implemented yet
