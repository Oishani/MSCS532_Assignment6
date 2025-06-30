# MSCS532 Assignment 6: Medians and Order Statistics & Elementary Data Structures

### Oishani Ganguly

This repository contains Python implementations of fundamental data structures (arrays, matrices, stacks, queues, linked lists, and trees) along with two selection algorithms (deterministic “median-of-medians” select and randomized select). It also includes benchmarking scripts, visualizations, comprehensive test suites, and result logs.

---

## Repository Structure  
```graphql
MSCS532_ASSIGNMENT6/
├── array.py                      # Dynamic array: insert, delete, access
├── matrix.py                     # 2D matrix: row insert/delete, get/set
├── stack.py                      # LIFO stack
├── queue.py                      # FIFO queue
├── linked_list.py                # Singly linked list
├── tree.py                       # Rooted tree using linked lists
│
├── deterministic_select.py       # Deterministic “select” (median-of-medians)
├── randomized_select.py          # Randomized selection (random pivot)
│
├── benchmark_selection.py        # Runs timing experiments, writes benchmark_results.csv
├── benchmark_results.csv         # Raw timing data
├── plot_benchmark.py             # Reads CSV and produces benchmark_plot.png
├── benchmark_plot.png            # Performance plot
│
├── test_data_structures.py       # Unit tests for arrays, matrices, stacks, queues, lists, trees
├── test_deterministic_select.py  # Unit tests for deterministic_select
├── test_randomized_select.py     # Unit tests for randomized_select
├── test_results_data_structures.txt  # Output from data-structures tests
├── test_results.txt              # Output from selection-algorithm tests
├── run_tests.sh                  # Shell script to run all selection algorithm tests and capture results
│
└── README.md                     # This file
```

---

## Requirements  
- **Python 3.7+**  
- **pip** packages:  
  ```bash
  pip3 install matplotlib pandas
  ```

---

## Running the Tests  
To verify correctness of the selection algorithms and capture results:

```bash
# Make the test script executable once:
chmod +x run_tests.sh

# Run all tests:
./run_tests.sh
```

This will generate (or overwrite) `test_results.txt`.

To verify correctness of the data structure implementations, run

```bash
python3 test_data_structures.py > test_results_data_structures.txt 2>&1
```

This will generate (or overwrite) `test_results_data_structures.txt`.

---

## Benchmarking Selection Algorithms  
1. **Generate raw timings**  
   ```bash
   python3 benchmark_selection.py
   ```  
   This populates `benchmark_results.csv` with timing data over various input sizes.

2. **Plot performance**  
   ```bash
   python3 plot_benchmark.py
   ```  
   Produces `benchmark_plot.png`, showing deterministic vs. randomized select runtimes.

---

## Summary of Findings  
- **Data Structures:**  
  - Arrays & Matrices deliver Θ(1) random-access and excellent cache locality.  
  - Linked Lists, Stacks, and Queues (array- or list-backed) offer Θ(1) insert/delete at ends but differ in memory overhead and access patterns.  
  - Trees provide hierarchical modeling and can be extended to balanced variants for Θ(log n) operations.

- **Selection Algorithms:**  
  - **Deterministic Select** guarantees worst-case Θ(n) time via median-of-medians, but with higher constant factors.  
  - **Randomized Select** achieves expected Θ(n) time with lower overhead, though rare worst-case Θ(n^2) partitions can occur.

Empirical benchmarks confirm that randomized selection is faster on average for random inputs, while the deterministic version remains steady regardless of input distribution.

---

## Report  
The final report `MSCS-532_ Assignment 6_ Medians and Order Statistics & Elementary Data Structures.pdf` includes comprehensive design rationales and implementation details for each data structure and selection algorithm, a clear description of the experimental methodology, detailed benchmark results with accompanying plots, formal time-and-space complexity analyses, and an in-depth discussion of performance trade-offs and real-world applications.
