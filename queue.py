class Queue:
    """FIFO queue implementation using a Python list as the underlying container."""
    def __init__(self):
        self._container = []

    def enqueue(self, item):
        self._container.append(item)

    def dequeue(self):
        if not self._container:
            raise IndexError("Dequeue from empty queue")
        return self._container.pop(0)

    def front(self):
        if not self._container:
            raise IndexError("Front from empty queue")
        return self._container[0]

    def is_empty(self):
        return len(self._container) == 0

    def size(self):
        return len(self._container)

    def __str__(self):
        return str(self._container)