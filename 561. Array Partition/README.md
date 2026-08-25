# Array Partition

**Difficulty:** Easy  
**Topic:** Array, Sorting, Greedy

## Problem

Given an integer array `nums` of `2n` elements, group these integers into `n` pairs `(a, b)` and maximize the sum of `min(a, b)` for all pairs.

## Approach

First, sort the array in ascending order.

After sorting, the optimal pairs can be formed by taking adjacent elements. The smaller element of each pair will be at an even index (`0, 2, 4, ...`).

So, we sort the array and sum the elements at even indices.

## Complexity

- Time: `O(n log n)`
- Space: `O(n)` (Python sorting)