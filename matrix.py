class Matrix:
    """A basic 2D matrix implementation with row insertion, deletion, and element access."""
    def __init__(self, rows, cols, default=None):
        self._rows = rows
        self._cols = cols
        self._data = [[default for _ in range(cols)] for _ in range(rows)]

    def insert_row(self, index, row_values=None):
        """Insert a new row at the specified index."""
        if index < 0 or index > self._rows:
            raise IndexError("Row index out of bounds")
        if row_values is None:
            row = [None] * self._cols
        elif len(row_values) != self._cols:
            raise ValueError(f"Row must have {self._cols} elements")
        else:
            row = list(row_values)
        self._data.insert(index, row)
        self._rows += 1

    def delete_row(self, index):
        """Delete and return the row at the specified index."""
        if index < 0 or index >= self._rows:
            raise IndexError("Row index out of bounds")
        row = self._data.pop(index)
        self._rows -= 1
        return row

    def get(self, row, col):
        """Get the element at (row, col)."""
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            raise IndexError("Index out of bounds")
        return self._data[row][col]

    def set(self, row, col, value):
        """Set the element at (row, col) to value."""
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            raise IndexError("Index out of bounds")
        self._data[row][col] = value

    def size(self):
        """Return (num_rows, num_cols)."""
        return (self._rows, self._cols)

    def __str__(self):
        return "\n".join(str(row) for row in self._data)
