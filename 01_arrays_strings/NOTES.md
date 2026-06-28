# 📦 Topic 01 — Arrays & Strings

## 🧠 Core Concepts

### What is an Array?
- An **ordered collection** of elements — same or mixed types (in Python)
- Python uses `list` as its array equivalent
- Elements are stored at **contiguous** memory locations (conceptually)
- Indexing starts at 0

```python
arr = [10, 20, 30, 40, 50]
#      0    1    2    3    4   ← positive index
#     -5   -4   -3   -2   -1  ← negative index
```

---

## ⏱️ Time Complexity — Array Operations

| Operation              | Time     | Note                              |
|------------------------|----------|-----------------------------------|
| Access by index        | O(1)     | `arr[i]`                          |
| Search (unsorted)      | O(n)     | Linear scan                       |
| Search (sorted)        | O(log n) | Binary search                     |
| Insert at end          | O(1)     | `arr.append(x)` amortized         |
| Insert at middle/start | O(n)     | Elements must shift               |
| Delete at end          | O(1)     | `arr.pop()`                       |
| Delete at middle/start | O(n)     | Elements must shift               |
| Slice `arr[i:j]`       | O(k)     | k = length of slice               |

---

## 🐍 Python List — Must-Know Tricks

```python
arr = [3, 1, 4, 1, 5, 9, 2, 6]

# Slicing
arr[1:4]      # [1, 4, 1]
arr[::-1]     # reverse → [6, 2, 9, 5, 1, 4, 1, 3]
arr[::2]      # every 2nd element → [3, 4, 5, 2]

# Common methods
arr.append(7)         # add to end — O(1)
arr.insert(0, 99)     # add at index — O(n)
arr.pop()             # remove last — O(1)
arr.pop(2)            # remove at index 2 — O(n)
arr.sort()            # in-place sort — O(n log n)
sorted(arr)           # returns new sorted list — O(n log n)
arr.count(1)          # count occurrences — O(n)
arr.index(5)          # first index of 5 — O(n)

# List comprehension
squares = [x**2 for x in range(10)]
evens   = [x for x in arr if x % 2 == 0]
```

---

## 📝 Strings — Key Points

```python
s = "hello world"

# Strings are IMMUTABLE in Python
# s[0] = 'H'  ← this will raise a TypeError

# Common operations
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.split()           # ["hello", "world"]
s.split(",")        # split by comma
" ".join(["a","b"]) # "a b"
s.strip()           # remove whitespace from both ends
s.replace("l","L")  # "heLLo worLd"
s.startswith("he")  # True
s.endswith("ld")    # True
s.find("world")     # 6 (index), returns -1 if not found
s.count("l")        # 3

# Trick: convert to list → modify → join back
chars = list(s)
chars[0] = 'H'
result = "".join(chars)  # "Hello world"
```

---

## 🔑 Patterns to Know (Topic 01)

### 1. Two Pointers
```
left = 0, right = len(arr) - 1
Move both pointers inward based on condition
Use case: sorted array, palindrome check, pair sum
```

### 2. Sliding Window
```
[  window  ] →
Maintain a window of elements and slide it forward
Use case: max subarray sum, longest substring
```

### 3. Frequency Map (Counter)
```python
from collections import Counter
freq = Counter("aabbcc")  # {'a':2, 'b':2, 'c':2}
```

### 4. Prefix Sum
```
prefix[i] = sum of arr[0..i]
Enables O(1) range sum queries after O(n) preprocessing
```

---

## 📌 2D Arrays (Matrix)

```python
# 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)      # 3
cols = len(matrix[0])   # 3

# Traverse all elements
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])

# Create a zero matrix using list comprehension
grid = [[0] * cols for _ in range(rows)]
# WARNING: Do NOT use [[0]*3]*3 — it creates shallow copies of the same row!
```

---

## 📂 Problems in this folder

| File | Problem | LC # | Difficulty | Pattern |
|------|---------|------|------------|---------|
| `two_sum.py` | Two Sum | #1 | Easy | Hash Map |
| `best_time_stocks.py` | Best Time to Buy/Sell Stock | #121 | Easy | Sliding Window |
| `easy_trio.py` | Contains Duplicate | #217 | Easy | Set |
| | Valid Anagram | #242 | Easy | Frequency Map |
| | Valid Palindrome | #125 | Easy | Two Pointers |
| `medium_duo.py` | Maximum Subarray | #53 | Medium | Kadane's Algorithm |
| | Product of Array Except Self | #238 | Medium | Prefix + Suffix |

---

## 🔗 Resources
- NeetCode Roadmap: https://neetcode.io/roadmap
- Python Docs (list): https://docs.python.org/3/tutorial/datastructures.html

---
