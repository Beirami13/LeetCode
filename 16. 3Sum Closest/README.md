# 3Sum Closest

**Difficulty:** Medium
**Topic:** Array, Sorting, Two Pointers

## Problem

Given an integer array `nums` and a `target`, find three different elements whose sum is closest to the target.

Return the sum of those three elements.

## Approach

First, sort the array.

Then, fix one number and use two pointers to find the other two numbers.

If the current sum is smaller than the target, move the left pointer forward to get a larger sum.

If the current sum is larger than the target, move the right pointer backward to get a smaller sum.

While doing this, keep track of the sum that is closest to the target.

If the sum is exactly equal to the target, return it immediately.

## Complexity

* Time: `O(n²)`
* Space: `O(n)` for sorting

## Solution

See [`16. 3Sum Closest.py`](./16.%203Sum%20Closest.py).
