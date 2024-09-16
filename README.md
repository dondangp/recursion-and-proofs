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
<img width="691" alt="Screenshot 2024-09-16 at 9 16 05 AM" src="https://github.com/user-attachments/assets/9ea0f05c-9eb2-4a19-aecd-eaa8a39d8bcc">

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
The time complexity for merging `K` sorted arrays is **O(N * log K)** using a priority queue or divide-and-conquer technique like merge sort. Here, `N` is the total number of elements across all arrays
<img width="754" alt="Screenshot 2024-09-16 at 9 46 36 AM" src="https://github.com/user-attachments/assets/511cf65b-ce2c-4de7-943b-2342a6f6e9cf">
.

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
## Time Complexity Proofs

### Problem 0: Fibonacci Sequence

The Fibonacci sequence implemented with recursion has an exponential time complexity. Here's why:

1. **Recursive Breakdown:**
   Each call to `fib(n)` results in two recursive calls:
   - `fib(n-1)` 
   - `fib(n-2)`

   Therefore, the recursive structure forms a binary tree with each level doubling the number of function calls. The number of calls increases exponentially with `n`.

2. **Recursion Tree:**
   If you draw out the recursion tree for `fib(n)`, you'll see that each node splits into two, creating a tree of depth `n`. The size of this tree, i.e., the total number of recursive calls, is proportional to `2^n`.

   For example:
   - `fib(5)` calls `fib(4)` and `fib(3)`.
   - `fib(4)` calls `fib(3)` and `fib(2)`, and so on.

3. **Overlapping Subproblems:**
   Many of the function calls are repeated multiple times. For instance, `fib(2)` and `fib(1)` are called multiple times throughout the tree. This inefficiency leads to an exponential number of recursive calls.

4. **Time Complexity:**
   Thus, the time complexity for this naive recursive implementation of the Fibonacci sequence is:
   T(n) = O(2^n)

   #### Optimization:
- **Memoization or Dynamic Programming** can reduce the time complexity to **O(n)** by storing the results of previously computed Fibonacci numbers.

---

### Problem 1: Merging K Sorted Arrays

When merging `K` sorted arrays, each containing `N` elements, we need to combine them while maintaining the sorted order. Let's analyze the time complexity:

1. **Naive Approach:**
A naive approach would involve merging two arrays at a time, repeatedly merging the result with the next array, one after another. This approach would result in **O(K * N^2)** time complexity because, at each step, you're remerging sorted arrays.

2. **Optimized Approach:**
Using **min-heaps (priority queues)** or a **divide-and-conquer** method (like in merge sort) optimizes the merging process:

- A min-heap can help identify the smallest element among all the arrays in constant time. Inserting and removing elements from the heap takes logarithmic time: **O(log K)**.

- The total number of elements being merged is `N * K` (since each array has `N` elements, and there are `K` arrays). Therefore, for each of the `N * K` elements, the heap operations take **O(log K)** time.

3. **Time Complexity:**
Combining the elements with heap operations, the time complexity is:
T(N, K) = O(N * K * log K)
This approach is much more efficient than the naive solution.

#### Optimization:
- Further improvements can be made by using more advanced data structures like balanced binary search trees, but the priority queue approach is already very efficient for this task.

---

### Problem 2: Removing Duplicates from a Sorted Array

Given a sorted array, the task is to remove duplicates in place and return only unique elements.

1. **Approach:**
The approach is to traverse the array once and move the unique elements forward while skipping over duplicates. Because the array is sorted, we know that all duplicates are adjacent to one another.

2. **Algorithm Breakdown:**
- Start at the second element of the array.
- Compare the current element with the previous one.
- If they are the same, skip the current element.
- If they are different, move the current element forward to the next available position for unique elements.

3. **Time Complexity:**
The algorithm requires a single pass over the array (of size `N`), performing constant time work at each step (i.e., comparing and moving elements).

Therefore, the time complexity is:
T(N) = O(N)
4. **Space Complexity:**
Since the problem specifies that the removal of duplicates should be done in place, the algorithm does not use any additional space apart from a few variables for indexing. Hence, the space complexity is:
S(N) = O(1)
#### Optimization:
- This solution is optimal in terms of time and space complexity, so no further improvements are necessary.
<img width="773" alt="Screenshot 2024-09-16 at 9 47 42 AM" src="https://github.com/user-attachments/assets/d834cf30-aa56-4dfa-a6b7-fa8814fa055b">

---

## Summary:

- **Problem 0 (Fibonacci Sequence):**  
Time Complexity: **O(2^n)**  
Optimized: **O(n)** (using memoization or dynamic programming)

- **Problem 1 (Merging K Sorted Arrays):**  
Time Complexity: **O(N * K * log K)**

- **Problem 2 (Removing Duplicates from a Sorted Array):**  
Time Complexity: **O(N)**  
Space Complexity: **O(1)**

## Using Constants to prove time complexity
# Problem 0: Fibonacci Sequence

### Task:
Implement the Fibonacci sequence recursively and debug the function call for `fib(5)`.

## Time Complexity Proof using Constants

Let's break down the recursive Fibonacci sequence in terms of time complexity:

1. **Base Case**:  
   If `n == 0` or `n == 1`, the function returns a constant value.  
   Therefore, the time complexity is `c1`, a constant time operation.

2. **Recursive Case**:  
   For `n > 1`, the Fibonacci function makes two recursive calls: `fib(n-1)` and `fib(n-2)`.  
   The time for each call can be represented as:
   T(n) = T(n-1) + T(n-2) + c2
Here, `c2` represents the constant time taken for the addition operation (`return fib(n-1) + fib(n-2)`).

3. **Recursion Tree**:  
This recursive structure creates a binary tree. Each level of the tree generates more recursive calls. In the worst case, the number of calls grows exponentially.

4. **Total Time Complexity**:  
Since each level of the recursion tree doubles the number of calls, the total time complexity is proportional to the number of nodes in the tree. The height of the tree is `n`, and the number of nodes is `O(2^n)`.

Thus, the time complexity can be expressed as:
T(n) = c1 + c2 * (2^n) = O(2^n)

Where `c1` is the base case time, and `c2` is the time per recursive step.

---

# Problem 1: Merging K Sorted Arrays

### Task:
Given `K` sorted arrays of size `N` each, merge them while maintaining their sorted order.

## Time Complexity Proof using Constants

We can analyze the time complexity using the following steps:

1. **Merging Two Arrays**:  
Merging two sorted arrays takes linear time proportional to the size of the arrays. If both arrays have `N` elements, merging them takes `c1 * N` time.

2. **Merging K Arrays**:  
To merge `K` arrays, we can use a **min-heap (priority queue)**. The heap allows us to find the smallest element among the arrays in logarithmic time (`log K`).  
For each element (a total of `N * K` elements), we perform the heap operation, which takes `c2 * log K` time.

3. **Total Time Complexity**:  
The total time complexity for merging all arrays is:
T(N, K) = c1 * (N * K) * log K = O(N * K * log K)
Where:
- `c1` is the time to merge two arrays,
- `c2` is the time for heap operations.

---

# Problem 2: Removing Duplicates from a Sorted Array

### Task:
Given a sorted array, remove the duplicate elements and return only unique elements.

## Time Complexity Proof using Constants

1. **Traverse the Array**:  
We start by traversing the sorted array once, comparing each element to the previous one to detect duplicates. This takes linear time, proportional to the size of the array `N`.

For each element, we perform a constant time comparison. This can be represented as `c1` time per comparison.

2. **Move Elements**:  
If a duplicate is found, we skip over it. Otherwise, we move the unique element forward to its correct position in the array. Moving each element is a constant time operation (`c2`), and we perform this operation for each element in the array.

3. **Total Time Complexity**:  
Since we traverse the array once and perform constant time operations on each element, the total time complexity is:
T(N) = c1 * N = O(N)
Where:
- `c1` is the time for each comparison,
- `c2` is the time for moving elements.

### Space Complexity:
The space complexity is `O(1)` since we are modifying the array in place without using extra space.

---

# Conclusion

- **Problem 0 (Fibonacci Sequence):**  
Time Complexity: **O(2^n)**, derived from the recursive tree structure where each level of recursion doubles the number of calls.

- **Problem 1 (Merging K Sorted Arrays):**  
Time Complexity: **O(N * K * log K)**, derived from merging arrays using a priority queue.

- **Problem 2 (Removing Duplicates from a Sorted Array):**  
Time Complexity: **O(N)**, since we traverse the array once and perform constant time operations on each element.
