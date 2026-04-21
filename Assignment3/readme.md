Sorting Performance Analyzer (SPA)

This project is part of the Data Structures (ETCCDS202) course. It focuses on implementing and analyzing different sorting algorithms to understand how they behave with different types of input data.

Objective
The main goal of this project is to compare the performance of three sorting algorithms:
Insertion Sort
Merge Sort
Quick Sort

The comparison is based on execution time and behavior for different dataset types.

Features
Implementation of sorting algorithms from scratch (no built-in sort functions used)
Dataset generation for:
Random data
Already sorted data
Reverse sorted data
Performance measurement using time functions
Comparison of results with theoretical time complexity
Output of results in a structured format
Algorithms Used
Insertion Sort

A simple sorting algorithm that builds the sorted array step by step. It works well for small or nearly sorted datasets but becomes slow for large inputs.

Merge Sort
A divide and conquer algorithm that splits the array into smaller parts, sorts them, and merges them back. It has consistent performance with O(n log n) time complexity.

Quick Sort
Another divide and conquer algorithm that selects a pivot and partitions the array. It performs very fast on average but can become slow in worst-case scenarios depending on pivot choice.

Dataset Details
The program generates datasets of the following sizes:
1000 elements
5000 elements
10000 elements

Each size includes:
Random data
Sorted data
Reverse sorted data
