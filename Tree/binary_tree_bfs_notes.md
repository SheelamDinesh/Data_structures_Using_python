# Binary Tree & BFS — Complete Interview Preparation Notes

---

## TABLE OF CONTENTS

1. Core Concepts
2. The 4 Traversal Types
3. BFS Deep Dive
4. All Code Patterns
5. Time & Space Complexity
6. BFS vs DFS — When to Use Which
7. Common Mistakes (from your code)
8. Interview Questions & Answers
9. Practice Problems
10. Memory Tricks & Mnemonics
11. What to Learn Next (Roadmap)

---

## 1. CORE CONCEPTS

### What is a Binary Tree?
- A tree where each node has at most 2 children (left and right)
- One root node at the top
- Nodes with no children are called LEAVES

### Key Terminology

    Term          | Meaning
    --------------|-----------------------------------------------------
    Root          | The top node (no parent)
    Leaf          | A node with no children
    Height        | Longest path from root to a leaf
    Depth         | Distance from root to a specific node
    Level         | Depth + 1 (root is at level 1)
    Subtree       | A node and all its descendants
    Parent        | The node directly above
    Sibling       | Nodes sharing the same parent

### Node Structure in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None    # left child
        self.right = None   # right child
```

### Building a Tree

```python
#        1         <- root (level 1)
#       / \
#      2   3       <- level 2
#     / \
#    4   5         <- level 3 (leaves)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

---

## 2. THE 4 TRAVERSAL TYPES

### Overview

    Traversal      | Type | Order                  | Output (for tree above)
    ---------------|------|------------------------|------------------------
    Level-Order    | BFS  | Level by level L→R     | 1 2 3 4 5
    Inorder        | DFS  | Left → Root → Right    | 4 2 5 1 3
    Preorder       | DFS  | Root → Left → Right    | 1 2 4 5 3
    Postorder      | DFS  | Left → Right → Root    | 4 5 2 3 1

### When to Use Each

- **Level-Order (BFS)** — shortest path, level-by-level processing
- **Inorder**           — gives SORTED output for BST
- **Preorder**          — copy/serialize a tree (root must come first)
- **Postorder**         — delete a tree, evaluate expression trees (children before parent)

---

## 3. BFS DEEP DIVE

### How it Works (Step by Step)

BFS uses a QUEUE (FIFO — First In, First Out).
Think of it like a ticket line. First person in = first person served.

```
Tree:   1
       / \
      2   3
     / \
    4   5

Start:  Queue = [1]         Output = ""
Step 1: Dequeue 1, print.   Enqueue 2, 3  →  Queue = [2, 3]     Output = "1"
Step 2: Dequeue 2, print.   Enqueue 4, 5  →  Queue = [3, 4, 5]  Output = "1 2"
Step 3: Dequeue 3, print.   No children   →  Queue = [4, 5]     Output = "1 2 3"
Step 4: Dequeue 4, print.   No children   →  Queue = [5]        Output = "1 2 3 4"
Step 5: Dequeue 5, print.   No children   →  Queue = []         Output = "1 2 3 4 5"
        Queue is empty → DONE
```

### Why Queue and NOT Stack?

- Queue (FIFO) → processes nodes in discovery order → visits level by level = BFS
- Stack (LIFO) → processes most recently added node first → goes deep = DFS
- Using a stack here would give you DFS, not BFS

### Why deque and NOT list?

```python
# DON'T use list
queue = []
queue.pop(0)      # O(n) — shifts ALL remaining elements, SLOW

# DO use deque
from collections import deque
queue = deque()
queue.popleft()   # O(1) — constant time, FAST
```

For 1 million nodes, list makes BFS O(n²). deque keeps it O(n).

---

## 4. ALL CODE PATTERNS

### Pattern 1 — Basic BFS (the correct version of your code)

```python
from collections import deque

def bfs(root):
    if root is None:           # always handle empty tree
        return

    queue = deque([root])      # initialise queue with root

    while queue:               # keep going until queue is empty
        node = queue.popleft() # O(1) remove from front
        print(node.data, end=" ")

        if node.left:          # only add non-None children
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### Pattern 2 — Level-by-Level BFS (very common in interviews)

```python
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)   # snapshot: how many nodes at THIS level
        level = []

        for _ in range(level_size):   # process exactly this level
            node = queue.popleft()
            level.append(node.data)

            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)

        result.append(level)

    return result

# Output: [[1], [2, 3], [4, 5]]
```

### Pattern 3 — All 3 DFS Traversals (Recursive)

```python
def inorder(root):       # Left → Root → Right
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    # Output: 4 2 5 1 3

def preorder(root):      # Root → Left → Right
    if not root:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
    # Output: 1 2 4 5 3

def postorder(root):     # Left → Right → Root
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
    # Output: 4 5 2 3 1
```

### Pattern 4 — BST Insert & Search

```python
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def search(root, val):
    if not root or root.data == val:
        return root
    if val < root.data:
        return search(root.left, val)
    return search(root.right, val)
```

### Pattern 5 — Tree Height

```python
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
```

### Pattern 6 — Iterative DFS (using explicit stack)

```python
def inorder_iterative(root):
    stack = []
    current = root
    result = []

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right

    return result
```

---

## 5. TIME & SPACE COMPLEXITY

    Operation            | Time  | Space  | Reason
    ---------------------|-------|--------|----------------------------------------
    BFS Traversal        | O(n)  | O(w)   | Visit every node once. Queue = one level
    DFS Traversal        | O(n)  | O(h)   | Visit every node once. Stack = one path
    Worst-case BFS space | O(n)  | O(n)   | Complete tree: last level has n/2 nodes
    Worst-case DFS space | O(n)  | O(n)   | Skewed tree (like linked list), h = n
    BST Search           | O(h)  | O(h)   | h = log n for balanced, n for skewed
    BST Insert           | O(h)  | O(h)   | Same as search

    n = total nodes, h = tree height, w = max width of tree

### Key Insight on Space
- Balanced tree → height h = log n → DFS uses O(log n) space
- Balanced tree → max width w ≈ n/2 → BFS uses O(n) space
- For balanced trees, DFS wins on memory

---

## 6. BFS vs DFS — WHEN TO USE WHICH

### Use BFS when:
- Finding shortest path between two nodes
- Processing nodes level by level
- Target node is likely near the root
- Finding all nodes at a specific depth

### Use DFS when:
- Exploring all possible paths (backtracking problems)
- Tree problems: inorder, preorder, postorder
- Checking tree properties (balanced, symmetric, valid BST)
- Target is likely deep in the tree
- Memory is a concern and tree is balanced

### Interview Answer Template
"I'd use BFS when I need level-by-level processing or shortest path, since
it guarantees visiting closer nodes first. I'd use DFS when I need to explore
all paths or when memory is a concern with a balanced tree, since DFS only
needs O(h) space vs O(w) for BFS."

---

## 7. COMMON MISTAKES (from your actual code)

### Mistake 1 — Recursive BFS (your original code)

```python
# WRONG — BFS should never be recursive
def binary_tree_traversal():
    if not queue:
        return None
    root = queue.popleft()
    print(root.data, end=" ")
    if root.left: queue.append(root.left)
    if root.right: queue.append(root.right)
    binary_tree_traversal()   # <-- recursion here is wrong
```

Why it's wrong:
- BFS is inherently iterative. Recursion adds unnecessary call stack overhead.
- Can hit Python's recursion limit (~1000) for large trees.
- Conceptually wrong — BFS uses a queue not a call stack.

### Mistake 2 — Global queue (your original code)

```python
# WRONG — queue lives outside the function
queue = deque()
queue.append(root_node)

def binary_tree_traversal():
    ...  # function depends on external state
```

Why it's wrong:
- Calling the function a second time won't work (queue is already empty).
- Function is tightly coupled to one specific tree.
- Not reusable, not testable, not thread-safe.

### Mistake 3 — Redundant check inside loop (your second version)

```python
# WRONG — dead code inside the loop
while queue:           # guarantees queue is NOT empty
    if not queue:      # this can NEVER be true
        return None
```

Why it's wrong:
- `while queue` already ensures queue has items.
- The `if not queue` check is unreachable code — remove it.

### Mistake 4 — Using parameter name but appending global (your third version)

```python
def binary_tree_traversal(root):      # parameter is 'root'
    queue = deque()
    queue.append(root_node)           # BUG: using global 'root_node' not parameter 'root'
```

Why it's wrong:
- Function ignores its own parameter entirely.
- Appears to work only because root_node still exists globally.
- Passing a different tree to the function would still process root_node.

### The Correct Final Version

```python
from collections import deque

def bfs(root):                    # accept root as parameter
    if root is None:              # handle empty tree
        return
    queue = deque([root])         # use parameter, not global

    while queue:                  # no redundant check needed
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)

bfs(root_node)                    # pass root explicitly
```

---

## 8. INTERVIEW QUESTIONS & ANSWERS

### Q1. What data structure does BFS use and why not a stack?

Answer:
BFS uses a queue (FIFO). We need to process nodes in the order they were
discovered — first discovered = first processed. A stack (LIFO) processes
the most recently added node first, which gives DFS. The queue ensures all
nodes at depth d are visited before any at depth d+1.

---

### Q2. Why use deque instead of list in Python for BFS?

Answer:
list.pop(0) is O(n) — it shifts all remaining elements left.
deque.popleft() is O(1) — implemented as a doubly-linked list.
For large trees, using list makes BFS O(n²) total vs O(n) with deque.

---

### Q3. When does DFS use less memory than BFS?

Answer:
On a balanced tree. DFS stack depth = height = O(log n).
BFS queue at the last level holds n/2 nodes = O(n).
Example: 1 million nodes → DFS uses O(20) space, BFS uses O(500,000).

---

### Q4. Can BFS be implemented recursively? Should it be?

Answer:
Technically yes, but it should never be done. BFS is inherently iterative.
Forcing recursion adds call stack overhead on top of the queue, gives no
benefit, and risks Python's recursion limit for deep trees.

---

### Q5. What is the difference between a Binary Tree and a BST?

Answer:
Binary Tree: any tree where each node has at most 2 children. No ordering rule.
BST (Binary Search Tree): a binary tree where for every node,
  all values in the LEFT subtree are LESS than the node's value, and
  all values in the RIGHT subtree are GREATER than the node's value.
BST allows O(log n) search on a balanced tree.

---

### Q6. Find the maximum depth of a binary tree

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
# O(n) time, O(h) space
```

---

### Q7. Check if a binary tree is symmetric

```python
def is_symmetric(root):
    def mirror(left, right):
        if not left and not right: return True
        if not left or not right:  return False
        return (left.data == right.data and
                mirror(left.left, right.right) and
                mirror(left.right, right.left))
    return mirror(root.left, root.right)
```

---

### Q8. Lowest Common Ancestor of two nodes

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left  = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root       # p on one side, q on other
    return left if left else right
```

---

### Q9. Validate a Binary Search Tree

```python
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if root.data <= lo or root.data >= hi:
        return False
    return (is_valid_bst(root.left, lo, root.data) and
            is_valid_bst(root.right, root.data, hi))

# Key insight: pass down valid range [lo, hi]
# Don't just compare with immediate parent — that's a classic mistake
```

---

### Q10. Right side view of a binary tree

```python
def right_side_view(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:    # last node of each level
                result.append(node.data)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
    return result
```

---

## 9. PRACTICE PROBLEMS

### EASY

**Problem 1 — Sum of all nodes**
Write a function that returns the sum of all node values.
Expected: sum_tree(root) = 15 (for 1+2+3+4+5)
Hint: return 0 for None, else root.data + sum(left) + sum(right)

**Problem 2 — Count all nodes**
Return the total number of nodes in the tree.
Hint: same structure as sum, but return 1 instead of root.data

**Problem 3 — Find maximum value**
Return the maximum value in a binary tree (not BST, any tree).
Hint: max(root.data, max_val(left), max_val(right))

**Problem 4 — Search in BST**
Return True if a value exists in a Binary Search Tree.
Hint: if val < root.data → go left. if val > root.data → go right.

---

### MEDIUM

**Problem 5 — Level order as list of lists**
Return a 2D list where each inner list has values at that level.
Expected: [[1], [2, 3], [4, 5]]
Hint: This is Pattern 2 exactly. Practice it from memory.

**Problem 6 — Check if tree is balanced**
A balanced tree has height difference <= 1 for EVERY node's subtrees.
Hint: return -1 as a sentinel for "unbalanced", propagate it up.

**Problem 7 — Root-to-leaf path sum**
Check if any root-to-leaf path sums to a given target.
Hint: subtract root.data from target. At a leaf, check if target == 0.

**Problem 8 — Invert a binary tree**
Mirror/flip the tree. Every left child becomes right and vice versa.
Hint: swap root.left and root.right, then recurse on both children.

---

### HARD

**Problem 9 — Diameter of a binary tree**
The diameter is the longest path between any two nodes.
Note: the path may NOT pass through the root.
Hint: diameter at a node = left_height + right_height.
      Track a global max as you compute heights using postorder.

**Problem 10 — Serialize and Deserialize a binary tree**
Convert a tree to a string (serialize) and reconstruct it (deserialize).
Asked at FAANG level.
Hint: Use preorder BFS with 'null' for None nodes.
      Serialize: "1,2,4,null,null,5,null,null,3,null,null"
      Deserialize: split by comma, reconstruct using a queue.

---

### Solutions to Easy Problems

```python
# Problem 1 — Sum
def sum_tree(root):
    if not root: return 0
    return root.data + sum_tree(root.left) + sum_tree(root.right)

# Problem 2 — Count
def count_nodes(root):
    if not root: return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Problem 3 — Max value
def max_val(root):
    if not root: return float('-inf')
    return max(root.data, max_val(root.left), max_val(root.right))

# Problem 4 — BST Search
def search_bst(root, val):
    if not root or root.data == val: return root
    if val < root.data: return search_bst(root.left, val)
    return search_bst(root.right, val)
```

---

## 10. MEMORY TRICKS & MNEMONICS

### Remember Traversal Orders

    Inorder   → "I'm in the MIDDLE"   → Left, ROOT, Right
    Preorder  → "PRE = before"        → ROOT, Left, Right  (root comes first)
    Postorder → "POST = after"        → Left, Right, ROOT  (root comes last)

### Visual Memory Anchors

    BFS = Birthday Party Seating
    Fill seats ROW BY ROW (level by level), not column by column.
    Queue = the line of guests waiting to be seated.

    DFS = Deep Sea Diver
    Goes as deep as possible on one path before coming back up.
    Stack = the rope tied to the diver (path back to surface).

    deque = Double-Door Bus
    Passengers can enter/exit from EITHER end in O(1).
    For BFS, popleft() is the EXIT door.
    Never use list.pop(0) — that's a slow revolving door.

    Tree Height = Building Floors
    Root = top floor. BFS visits one complete floor before going down.

### The 5-Point Code Checklist (before every tree problem)

    1. Handle None/empty tree at the start
    2. Pass root as a parameter (never use globals)
    3. Use deque, not list (for O(1) popleft)
    4. No redundant checks inside the while loop
    5. Only append non-None children to the queue

### Complexity Quick Reference

    BFS → O(n) time, O(w) space   where w = max width
    DFS → O(n) time, O(h) space   where h = height
    Balanced tree → h = log n, w = n/2  → DFS wins on space
    Skewed tree   → h = n,     w = 1    → BFS wins on space

---

## 11. WHAT TO LEARN NEXT (ROADMAP)

### Step 1 — DFS Iterative (all 3 traversals without recursion)
You know recursive DFS. Now learn iterative DFS using an explicit stack.
Required to handle deep trees without hitting Python's recursion limit.
Inorder iteratively is a classic interview question.

### Step 2 — BST Operations (Insert, Delete, Search)
Understand the BST property: left < root < right.
Deletion is the hardest — need inorder successor for nodes with 2 children.

### Step 3 — Tree Height, Depth, Diameter
Most common warm-up questions. Practice until you can write from memory in 2 min.
Height → postorder DFS. Diameter → track global max during height calculation.

### Step 4 — Path Problems (root-to-leaf, any path)
Path sum, all root-to-leaf paths, maximum path sum (hardest).
These build on DFS but require carrying state down the recursion.

### Step 5 — LCA (Lowest Common Ancestor)
Favourite at Google, Amazon, Meta.
BST LCA: use value comparisons.
General binary tree LCA: postorder search.

### Step 6 — Serialize / Deserialize a Tree
Asked at FAANG level. Use preorder traversal + null markers.
Tests deep understanding of tree structure and reconstruction.

### Step 7 — Balanced Trees (AVL concept)
Understand what self-balancing means and why O(log n) operations matter.
You don't need to implement AVL rotations for most interviews.

---

### Recommended LeetCode Problems (in order)

    #102  Binary Tree Level Order Traversal    ← do this first
    #104  Maximum Depth of Binary Tree
    #226  Invert Binary Tree
    #543  Diameter of Binary Tree
    #112  Path Sum
    #98   Validate Binary Search Tree
    #101  Symmetric Tree
    #236  Lowest Common Ancestor of a Binary Tree
    #297  Serialize and Deserialize Binary Tree  ← hardest, do last

---

## QUICK REFERENCE CARD

```
CREATE TREE          BUILD QUEUE           BFS LOOP
-----------          -----------           --------
class Node:          from collections      while queue:
  def __init__         import deque            node = queue.popleft()
    self.data = d    queue = deque()            process(node)
    self.left = None queue.append(root)         if node.left:
    self.right= None                               queue.append(node.left)
                                               if node.right:
                                                  queue.append(node.right)

INORDER              PREORDER              POSTORDER
-------              --------              ---------
inorder(left)        print(root)           postorder(left)
print(root)          preorder(left)        postorder(right)
inorder(right)       preorder(right)       print(root)
→ sorted BST         → copy/serialize      → delete/evaluate
```

---
