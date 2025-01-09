
---

### **10. Dynamic Programming: Fibonacci Sequence, Longest Common Subsequence, Knapsack Problem**

#### **Markdown File (`dynamic_programming.md`)**
```markdown
# Dynamic Programming Operations: Fibonacci, LCS, Knapsack

### Introduction
**Dynamic Programming (DP)** is a method for solving problems by breaking them down into simpler subproblems and solving each subproblem only once. It is particularly useful for optimization problems.

### Methods:
1. **Fibonacci Sequence**: Compute the nth Fibonacci number.
2. **Longest Common Subsequence (LCS)**: Find the longest common subsequence between two strings.
3. **Knapsack Problem**: Solve the 0/1 knapsack problem to maximize the value of items that can fit into a knapsack of a given capacity.

### Python Code:
```python
# Fibonacci Sequence using DP (Memoization)
def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Longest Common Subsequence using DP
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Knapsack Problem using DP
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage
print("Fibonacci(10):", fibonacci(10))
print("LCS of 'ABCBDAB' and 'BDCABB':", lcs('ABCBDAB', 'BDCABB'))
print("Knapsack Problem Solution:", knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))
