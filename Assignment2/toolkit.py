"""
Linear Data Structures Toolkit (LDST)
Data Structures - Unit 2 Assignment

School:             School of Engineering & Technology 
Program: 					  B.Tech CSE (AI and ML) 
Course Title:				Data Structures 
Course Code:				ETCCDS202 
Unit Title:					Linear Data Structures

Student Name:				Bhavya Shany 
Roll Number:				2501730024
Section:					  A 
Semester:					  2 
Batch:					    2025-26 
Submitted To:				Mrs. Neetu Chauhan 
"""



# Task 1: DYNAMIC ARRAY OPERATIONS



class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            print(f"Resizing from {self.capacity} to {self.capacity * 2}")
            self.resize()

        self.arr[self.size] = x
        self.size += 1

    def resize(self):
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def __str__(self):
        return str([self.arr[i] for i in range(self.size)])





# TASK 2 : LINKED LIST OPERATIONS


# Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, x):
        new_node = Node(x)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
        else:
            print("Value not found")

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)





# Doubly Linked List


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = DNode(x)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = DNode(x)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next

        print("Target not found")

    def delete_position(self, pos):  # 0-based
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)





# TASK 3 : STACK AND QUEUE FROM SCRATCH
# ---------------------------------

# Stack using SLL


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            print("Stack Underflow")
            return None

        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data





# Queue using SLL


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)

        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            print("Queue Underflow")
            return None

        val = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data





# TASK 4 : APPLICATION
# ---------------------

# Parentheses Checker


def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.peek() != pairs[ch]:
                return False
            stack.pop()

    return stack.head is None







# MAIN CODE RUNNER
# ------------------


if __name__ == "__main__":

    print()
    print(" Dynamic Array ")
    ds = DynamicArray(2)
    for i in range(12):
        ds.append(i)
        print(ds)

    print("Pop:", ds.pop())
    print("Pop:", ds.pop())
    print("Pop:", ds.pop())
    print(ds)

    print()
    print("\n Singly Linked List ")
    sll = SinglyLinkedList()
    sll.insert_beginning(10)
    sll.insert_beginning(20)
    sll.insert_beginning(30)
    sll.traverse()

    sll.insert_end(40)
    sll.insert_end(50)
    sll.insert_end(60)
    sll.traverse()

    sll.delete_value(40)
    sll.traverse()

    print("\n Doubly Linked List ")
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.traverse()

    dll.insert_after(2, 99)
    dll.traverse()

    dll.delete_position(1)
    dll.traverse()

    print()
    print("\n Stack ")
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print("Pop:", st.pop())
    print("Peek:", st.peek())

    print()
    print("\n Queue ")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Dequeue:", q.dequeue())
    print("Front:", q.front())

    print()
    print("\n Parentheses Check ")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "-", "Balanced" if is_balanced(t) else "Not Balanced")

   
