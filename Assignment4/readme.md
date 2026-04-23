# 📊 Data Management Mini Toolkit (DMMT)

## 📌 Overview

This project is a Python-based mini toolkit that demonstrates the implementation of important data structures used in real-world systems:

* Binary Search Tree (BST)
* Graph (Adjacency List with BFS & DFS)
* Hash Table (with Separate Chaining)

The goal is to understand how efficient data storage, searching, and traversal work in practical applications.

---

## 🚀 Features

### 🔹 Binary Search Tree (BST)

* Insert elements
* Search elements
* Delete nodes (all cases: leaf, one child, two children)
* Inorder traversal (sorted output)

---

### 🔹 Graph

* Directed and weighted graph
* Adjacency list representation
* Breadth First Search (BFS)
* Depth First Search (DFS)

---

### 🔹 Hash Table

* Custom hash function: `key % table_size`
* Collision handling using **separate chaining**
* Insert, get, and delete operations

---

## 🛠️ Technologies Used

* Python (Basic concepts only, no advanced libraries)

---

## ▶️ How to Run

1. Make sure Python is installed
2. Open terminal in project folder
3. Run the file:

```bash
python dmmt_toolkit.py
```

---

## 📂 Project Structure

```
DMMT/
│── dmmt_toolkit.py   # Main implementation file
│── report.pdf        # Explanation of concepts
│── output.txt        # Program output
│── README.md         # Project documentation
```

---

## 🧪 Test Cases Included

### BST

* Insert: 50, 30, 70, 20, 40, 60, 80
* Search: 20, 90
* Delete:

  * Leaf node → 20
  * One child → 60 (after inserting 65)
  * Two children → 30

---

### Graph

* Nodes: A, B, C, D, E, F
* BFS and DFS traversal from node A

---

### Hash Table

* Table size: 5
* Keys inserted: 10, 15, 20, 7, 12
* Demonstrates collision handling

---

## 📖 Concepts Covered

* Tree traversal and operations
* Graph traversal algorithms (BFS & DFS)
* Hashing and collision resolution

---

## ⚡ Learning Outcome

This project helps in understanding:

* Efficient data storage using BST
* Network traversal using graphs
* Fast lookup using hash tables

---

## 📎 Notes

* No built-in dictionary is used for hash table logic
* Graph is implemented using adjacency list
* Code is written in simple Python for learning purposes

---

## 🙌 Author

* Name: Bhavya Shany
* Course: B.Tech CSE (AI & ML)
* Subject: Data Structures

---

## 📚 References

* Classroom notes
* GeeksforGeeks
* Data Structures textbooks

---

