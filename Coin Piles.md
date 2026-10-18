## 01. Coin Piles

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/coin-piles5152/1)

### Problem Description

**Task:** You are given an array arr[] of integers, where each element represents the number of coins in a pile. You are also given an integer k.Your task is to remove the minimum number of coins such that the absolute difference between the number of coins in any two updated piles is at most k.

> **Note:** You can also remove a pile by removing all the coins of that pile.

#### Examples

##### Example 1

- **Input:**
```text
arr[] = [2, 2, 2, 2], k = 0
```
- **Output:**
```text
0
```
- **Explanation:** For any two piles the difference in the number of coins is <= 0. So no need to remove any coin.

##### Example 2

- **Input:**
```text
arr[] = [1, 5, 1, 2, 5, 1], k = 3
```
- **Output:**
```text
2
```
- **Explanation:** If we remove one coin each from both the piles containing 5 coins, then for any two piles the absolute difference in the number of coins is <= 3.

#### Constraints

- **1.** `1 ≤ arr.size() ≤ 10⁵¹ ≤ arr[i] ≤ 10⁴^0 ≤ k ≤ 10⁴`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-18 21:09:22
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        ans = float('inf')
        prev_removed = 0

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                prev_removed += arr[i - 1]
                continue

            low, high = i, n - 1
            idx = i
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= arr[i] + k:
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1

            removed_left = prev_removed
            removed_right = prefix_sum[n] - prefix_sum[idx + 1] - (n - 1 - idx) * (arr[i] + k)
            ans = min(ans, removed_left + removed_right)

            prev_removed += arr[i]

        return ans
```

*Generated on: 18/10/2026, 21:09:40*