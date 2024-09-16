## Problem 0: Fibonacci Sequence

### Task:
Implement the Fibonacci sequence recursively and debug the function call for `fib(5)`.

### Breakdown of how each recursive step works for `fib(5)`:

- First, `fib(5)` calls both `fib(4)` and `fib(3)`.

- Then, `fib(4)` calls both `fib(3)` and `fib(2)`.

- Then, `fib(3)` calls both `fib(2)` and `fib(1)`.

- `fib(2)` further calls `fib(1)` and `fib(0)`, which return `1` and `0` respectively.

- Therefore, `fib(2)` returns `1`, and `fib(3)` returns `2` after summing up `fib(2)` and `fib(1)`.

- Moving back to `fib(4)`, the value `2` from `fib(3)` is added to the value returned by `fib(2)` (which is `1`), resulting in `fib(4)` returning `3`.

- Finally, back in `fib(5)`, the results from `fib(4)` and `fib(3)` are summed (i.e., `3 + 2`), yielding the final output of `5`.

### (A more detailed explanation of the function call stack is included in the `fib.py` file)

### Time Complexity of Fibonacci Code:
The time complexity of the recursive Fibonacci code is **O(2^n)**, which is exponential.

#### Reasons:
##### Recursive Calls:
- For each call to `fib(n)`, the function makes two recursive calls: `fib(n-1)` and `fib(n-2)`. This branching happens at every level, resulting in a large number of repeated calculations.

##### Overlapping Subproblems:
- Many Fibonacci numbers are recalculated multiple times. For example, `fib(2)` and `fib(1)` are computed multiple times across the recursion tree. This duplication of work grows rapidly as `n` increases.

### Ways to Improve the Fibonacci Implementation:

#### 1. Memoization:
- We can create a memory (dictionary or array) to store the calculated results so that we avoid recalculating them. This reduces the time complexity to **O(n)**, considering **O(1)** time to fetch the values of precomputed ones from the memory.

#### 2. Dynamic Programming:
- We can simply use arrays and store the results and iterate up to `n`. Even this approach can achieve **O(n)** time complexity.

---

## Problem 1: Merge K Sorted Arrays

### Task:
Given `K` sorted arrays of size `N` each, merge them while maintaining their sorted order.

### Example 1:
- **Input:**
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
- **Output:**
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
### Example 2:
- **Input:**
array1 = [1, 3, 7]
array2 = [2, 4, 8]
array3 = [9, 10, 11]
- **Output:**
[1, 2, 3, 4, 7, 8, 9, 10, 11]
### Time Complexity of the Solution:
The time complexity for merging `K` sorted arrays is **O(N * log K)** using a priority queue or divide-and-conquer technique like merge sort. Here, `N` is the total number of elements across all arrays.

### (Implementation is in the `merge_sort.py` file)

---

## Problem 2: Remove Duplicates from a Sorted Array

### Task:
Given a sorted array, remove the duplicate elements from the array and return only unique elements.

### Example 1:
- **Input:**  
`array = [2, 2, 2, 2, 2]`
- **Output:**  
`array = [2]`

### Example 2:
- **Input:**  
`array = [1, 2, 2, 3, 4, 4, 4, 5, 5]`
- **Output:**  
`array = [1, 2, 3, 4, 5]`

### Time Complexity of the Solution:
The time complexity for removing duplicates from a sorted array is **O(N)** since each element is processed once. We simply traverse the array once and skip over duplicates as we go.

### (Implementation is in the `remove_duplicates.py` file)

---

## Conclusion:
- The problems involve solving recursive Fibonacci, merging sorted arrays, and removing duplicates from a sorted array.
- Each problem includes the expected outputs, explanations of the function call stacks, and time complexity analyses.
- Screenshots of the output will be added after running the code.

---

## How to Run:
1. Clone the repository.
2. Run the individual Python files (`fib.py`, `merge_sort.py`, `remove_duplicates.py`) to see the outputs.
3. The images of the function call stack and outputs will be included in future updates.
