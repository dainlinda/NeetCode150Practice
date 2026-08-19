# Approach

## Check conditions to meet

BST: left < root < right (all val is unique so not <= or >=)
num nodes: 2 to 100 (p or q can be root, but p != q and both exist)
val nodes: -100 to 100

## Key idea
ancestor changes when p and q diverge

## Pseudo code 
- goal: start from working code to optimized code

```
var ancestor = root
while searching for p and q
    if p,q < node or node < p,q && node != p or q
        update var ancestor
    else  # diverge or node == p or q
        return var at the moment
return var ancestor when p and q were found
```

## Complexity
time: assume a complete tree, p,q diverge from root, and both are located at leaves
root + then only check ... 2 among 2^1 + 2 among 2^2 + ... + 2 among 2^h = O(1 + 2*h) = O(h)

space: O(1) since no additional ds is used except for a single var

## correctness check
test cases
root = [5,3,8,1,4,7,9,null,2]
- p = 3, q = 8 => 5 # else, found both, return root
- p = 3, q = 4 => 3 # if, update ancester = 3 (found p), found q, return 3
- p = 1, q = 9 => 5 # else, so return root
- p = 2, q = 4 => 3 # if, update ancester = 3, found q and p should diverge so return 3

any edge cases?
- check smallest input
root = [1,2] p = 1, q = 2 => else return ancestor = 1
