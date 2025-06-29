def deterministic_select(arr, k):
    """
    Return the k-th smallest element of array arr (1-based k).
    Uses the median-of-medians pivot rule to guarantee O(n) worst-case time.
    Raises ValueError if k is out of range.
    """
    n = len(arr)
    if k < 1 or k > n:
        raise ValueError("k is out of bounds")

    # Base case: small array, just sort
    if n <= 5:
        return sorted(arr)[k-1]

    # 1. Partition arr into groups of 5 and find each group's median.
    medians = []
    for i in range(0, n, 5):
        group = arr[i:i+5]
        medians.append(sorted(group)[len(group)//2])

    # 2. Recursively find the true median of the medians.
    pivot = deterministic_select(medians, len(medians)//2 + 1)

    # 3. Partition around pivot
    lows  = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # 4. Recurse into the appropriate part
    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))
