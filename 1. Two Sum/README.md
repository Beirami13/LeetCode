# Two Sum

**Difficulty:** Easy  
**Topic:** Array, Hash Table
**Problem:** [Two Sum — LeetCode](https://leetcode.com/problems/two-sum/description/)

## Problem

Given an array of integers `nums` and an integer `target`, find two numbers that add up to the target.

Return their indices.

## Approach

Check each pair of numbers in the array.

For each number, compare it with the numbers that come after it. If their sum equals the target, return their indices.

## Complexity

- Time: `O(n²)`
- Space: `O(1)`

## Solution

See [`1. Two Sum.py`](./1.%20Two%20Sum.py).