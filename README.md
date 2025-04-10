# Most Beautiful Item for Each Query

## Problem Description

You are given a 2D integer array `items` where `items[i] = [price_i, beauty_i]` represents the price and beauty of the `i`-th item, respectively.

You are also given a 0-indexed integer array `queries`. For each query `queries[j]`, you need to determine the maximum beauty of an item whose price is less than or equal to `queries[j]`. If no such item exists, the answer to this query is `0`.

Return an array `answer` of the same length as `queries`, where `answer[j]` is the answer to the `j`-th query.

---

## Example 1:

### Input:

```python
items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries = [1, 2, 3, 4, 5, 6]
```
### Output:
[2, 4, 5, 5, 6, 6]

### Explanation:
+ For queries[0] = 1, the only item with price ≤ 1 is [1, 2]. Hence the answer is 2.

+ For queries[1] = 2, the items that can be considered are [1, 2] and [2, 4]. The maximum beauty is 4.

+ For queries[2] = 3 and queries[3] = 4, the items that can be considered are [1, 2], [3, 2], [2, 4], [3, 5]. The maximum beauty is 5.

+ For queries[4] = 5 and queries[5] = 6, all items can be considered. The maximum beauty is 6.

### Constraints:
+ 1 <= items.length, queries.length <= 10^5

+ items[i].length == 2

+ 1 <= price_i, beauty_i, queries[j] <= 10^9
