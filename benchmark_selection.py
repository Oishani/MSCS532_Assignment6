import time
import random
import csv
from deterministic_select import deterministic_select
from randomized_select import randomized_select

def generate_input(size, distribution):
    """Generate an array of given size and distribution."""
    if distribution == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reverse':
        return list(range(size, 0, -1))
    else:
        raise ValueError(f"Unknown distribution: {distribution}")

def time_algorithm(func, arr, k):
    """Time a single call to func(arr, k). Returns (elapsed_seconds, result)."""
    start = time.perf_counter()
    result = func(arr, k)
    end = time.perf_counter()
    return end - start, result

def main():
    random.seed(0)
    sizes = [1_000, 5_000, 10_000, 20_000]
    distributions = ['random', 'sorted', 'reverse']
    algorithms = [
        ('deterministic', deterministic_select),
        ('randomized', randomized_select),
    ]
    trials = 5

    rows = []
    print(f"{'algorith m':12s} | {'dist':8s} | {'n':6s} | {'avg_time (s)':>12s}")
    print("-"*46)

    for n in sizes:
        for dist in distributions:
            base = generate_input(n, dist)
            k = n // 2  # always select the median
            for name, func in algorithms:
                times = []
                for _ in range(trials):
                    arr = base.copy()
                    t_elapsed, res = time_algorithm(func, arr, k)
                    times.append(t_elapsed)
                avg = sum(times) / trials
                rows.append({
                    'algorithm': name,
                    'distribution': dist,
                    'size': n,
                    'avg_time_s': avg
                })
                print(f"{name:12s} | {dist:8s} | {n:6d} | {avg:12.6f}")

    # write out CSV for easy table creation
    with open('benchmark_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['algorithm','distribution','size','avg_time_s'])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
