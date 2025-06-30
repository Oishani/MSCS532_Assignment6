class Array:
    """A simple dynamic array implementation supporting insertion, deletion, and access."""
    def __init__(self):
        self._data = []

    def insert(self, index, value):
        """Insert value at the given index."""
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of bounds")
        self._data.insert(index, value)

    def delete(self, index):
        """Delete and return the element at index."""
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data.pop(index)

    def access(self, index):
        """Return the element at index without removing it."""
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def size(self):
        """Return the number of elements in the array."""
        return len(self._data)

    def __str__(self):
        return str(self._data)
