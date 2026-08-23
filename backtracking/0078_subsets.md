
# Approach

## Check conditions to meet

- input: an array `nums`
  - unique integers
  - len: 1 to 10
  - val: -10 to 10
- return: all possible subsets of `nums`
  - no duplicate
  - any order

## Key idea

- Inspired by: https://backtrack-visualize.vercel.app/subsets.html
  - explore all combinations of nums recursively, strictly increasing the num

```
# when input = [1,2,3]
# different start point
dfs(1)
    -> dfs(2)  dfs(3)
    -> dfs(3)
dfs(2)
    -> dfs(3)
dfs(3)
- can only call larger num than curr
```


## Pseudo code

```
result = [[]] # start with empty list
def dfs(arglist = []): # accumulate to children
    result.append(arglist)
    curr = arglist[-1]
    # call anything larger than me
    dfs(curr + 1)
    dfs(curr + 2)
    dfs(curr + ...)

n = len(nums)
for i in n:
    dfs([i])
```

## Complexity
- time: O(2^n) for dfs call (# subsets) * O(n) task for creating new combination list per dfs call = O(n*2^n)
  - this is already a lower bound of the problem because the total work overall is sum(k * C(n,k)) when k is 0 to n = n * 2^(n-1)
- space: auxiliary space is O(n) for recursive stack, but each recursive stack holds O(n) for new combination list = O(n^2)
 
## Caveat and Reflection (Claude-assisted)

- Space optimization: use only one list mutating in place. 
  - when append to result, use combination[:] to create a new object of the current combination so that it's not affected by mutation.
    - which costs O(k) at that node but doesn't accumulate across the stack, since it's not carried in the frame itself.
  - therefore, auxiliary space is O(n), only the recursion stack depth.