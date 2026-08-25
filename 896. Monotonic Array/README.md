# Monotonic Array

**Difficulty:** Easy  
**Topic:** Array

## Problem

Given an integer array `nums`, determine if the array is monotonic.

An array is monotonic if it is either entirely non-increasing or entirely non-decreasing.

## Approach

Use two boolean variables to track whether the array can still be increasing or decreasing.

Iterate through the array and compare each element with the next one.

- If `nums[i] > nums[i + 1]`, the array cannot be increasing.
- If `nums[i] < nums[i + 1]`, the array cannot be decreasing.

If either condition remains possible after checking the entire array, return `True`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`
