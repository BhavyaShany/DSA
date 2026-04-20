
# 📦 Linear Data Structures Toolkit (LDST)

> **Course:** Data Structures (ETCCDS202) — Unit 2 Assignment  
> **Student:** Bhavya Shany | **Roll No.:** 2501730024 | **Section:** A  
> **Program:** B.Tech — School of Engineering & Technology

---

## 📁 Project Structure

```
LDST_Assignment_2501730024_BhavyaShany/
│
├── ldst_toolkit.py      # All implementations + main runner
├── report.pdf           # Complexity analysis & amortized explanation
├── output.txt           # Console output for all test cases
└── README.md            # This file
```

---

## 🧩 What's Implemented

### 1. 🔢 Dynamic Array
- Custom `DynamicArray` class with internal capacity tracking
- `append(x)` — doubles capacity when full (amortized O(1))
- `pop()` — removes and returns the last element
- Shows resize events with size/capacity at each step

### 2. 🔗 Singly Linked List
- `insert_at_beginning(x)` — O(1)
- `insert_at_end(x)` — O(n)
- `delete_by_value(x)` — O(n)
- `traverse()` — prints all elements

### 3. ↔️ Doubly Linked List
- Extends Singly Linked List
- `insert_after_node(target, x)` — inserts after first occurrence of target
- `delete_at_position(pos)` — 0-based index deletion
- Maintains `prev` and `next` pointers correctly

### 4. 📚 Stack ADT (LIFO)
- Built on top of `SinglyLinkedList`
- `push(x)`, `pop()`, `peek()` — all O(1)
- Operates at head for efficiency
- Handles underflow safely

### 5. 🚶 Queue ADT (FIFO)
- Built on top of `SinglyLinkedList`
- `enqueue(x)`, `dequeue()`, `front()` — all O(1)
- Uses both `head` and `tail` pointers
- Handles underflow safely

### 6. ✅ Balanced Parentheses Checker
- Uses the custom `Stack` (not Python's built-in list)
- Supports `()`, `{}`, `[]`
- Returns `True` / `False`

---

## ▶️ How to Run

```bash
python ldst_toolkit.py
```

---

## 🧪 Test Cases

### Dynamic Array
| Action | Result |
|--------|--------|
| Append 10+ items (capacity starts at 2) | Resize happens at 2→4→8→16 |
| Pop 3 times | Last 3 elements removed |

### Singly Linked List
| Action | Result |
|--------|--------|
| Insert 3 at beginning, 3 at end | List grows correctly |
| Delete by value | Node removed, list intact |

### Doubly Linked List
| Action | Result |
|--------|--------|
| Insert after target node | Prev/next links maintained |
| Delete at position 1 and last | Correct node removed |

### Stack & Queue
| Operation | Expected |
|-----------|----------|
| push/pop/peek | LIFO order |
| enqueue/dequeue/front | FIFO order |

### Balanced Parentheses Checker
| Expression | Output |
|------------|--------|
| `([])`     | ✅ Balanced |
| `([)]`     | ❌ Not Balanced |
| `(((`      | ❌ Not Balanced |
| `""`       | ✅ Balanced |

---

## 📊 Time Complexity Summary

| Data Structure | Operation | Complexity |
|----------------|-----------|------------|
| Dynamic Array | append() amortized | O(1) |
| Dynamic Array | pop() | O(1) |
| Singly Linked List | insert_at_beginning() | O(1) |
| Singly Linked List | insert_at_end() | O(n) |
| Singly Linked List | delete_by_value() | O(n) |
| Doubly Linked List | insert_after_node() | O(n) |
| Doubly Linked List | delete_at_position() | O(n) |
| Stack | push / pop / peek | O(1) |
| Queue | enqueue / dequeue / front | O(1) |
| Parentheses Checker | is_balanced() | O(n) |

---

## 📚 References

- Cormen et al., *Introduction to Algorithms*, 3rd ed., MIT Press
- [GeeksforGeeks – Dynamic Array](https://www.geeksforgeeks.org/dynamic-array/)
- [GeeksforGeeks – Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [GeeksforGeeks – Stack](https://www.geeksforgeeks.org/stack-data-structure/)
- [GeeksforGeeks – Queue](https://www.geeksforgeeks.org/queue-data-structure/)

---

> 🔒 *All code and report written independently as per academic integrity guidelines.*
