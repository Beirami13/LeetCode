# Candy

**Difficulty:** Hard  
**Topic:** Array, Greedy

## Problem

Each child must get at least one candy. If a child has a higher rating than their neighbor, they must get more candies than that neighbor.

The goal is to give out the minimum number of candies while following these rules.

## Approach

Start by giving every child one candy.

Go through the ratings from left to right. If a child has a higher rating than the child before them, give them one more candy than the previous child.

Then go through the array from right to left to check the other neighbors. If a child has a higher rating than the child after them, make sure they have more candies too.

Finally, return the total number of candies.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

See [`135. Candy.py`](./135.%20Candy.py).