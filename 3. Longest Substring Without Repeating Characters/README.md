# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Topic:** String, Hash Table, Sliding Window

## Problem

Given a string `s`, find the length of the longest substring that does not contain any repeated characters.

For example, in `"abcabcbb"`, the longest substring without repeating characters is `"abc"`, so the answer is `3`.

## Approach

Start from each character and build the substring one character at a time.

A `set` is used to keep track of the characters that are already in the current substring. If a character is already in the set, we stop building that substring and move to the next starting position.

While doing this, we keep the longest length we have found.

## Complexity

* Time: `O(n²)`
* Space: `O(n)`

## Solution

See [`3. Longest Substring Without Repeating Characters.py`](./3.%20Longest%20Substring%20Without%20Repeating%20Characters.py).
