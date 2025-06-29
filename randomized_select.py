import random

def randomized_select(arr, k):
    """
    Return the k-th smallest element of array arr (1-based k).
    Uses random pivot selection for expected O(n) time.
    Raises ValueError if k is out of range.
    """
    n = len(arr)
    if k < 1 or k > n:
        raise ValueError("k is out of bounds")

    # Base case
    if n == 1:
        return arr[0]

    # 1. Pick a random pivot
    pivot = random.choice(arr)

    # 2. Partition around pivot
    lows  = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # 3. Recurse
    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))
