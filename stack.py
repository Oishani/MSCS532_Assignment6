class Stack:
    """LIFO stack implementation using a Python list as the underlying container."""
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        if not self._container:
            raise IndexError("Pop from empty stack")
        return self._container.pop()

    def peek(self):
        if not self._container:
            raise IndexError("Peek from empty stack")
        return self._container[-1]

    def is_empty(self):
        return len(self._container) == 0

    def size(self):
        return len(self._container)

    def __str__(self):
        return str(self._container)
