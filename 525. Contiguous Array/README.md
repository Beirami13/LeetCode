# Contiguous Array

**Difficulty:** Medium  
**Topic:** Array, Hash Table, Prefix Sum

## Problem

Given a binary array `nums`, find the maximum length of a contiguous subarray with an equal number of `0` and `1`.

## Approach

Treat `0` as `+1` and `1` as `-1`.

Keep a running `count` while iterating through the array.

If the same `count` appears at two different indices, the elements between those indices contain an equal number of `0` and `1`.

Store the first index where each `count` appears in a hash table. When the same `count` appears again, calculate the length of the subarray and keep the maximum length found.

The initial value is stored as `0: -1` to handle balanced subarrays that start from index `0`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`
