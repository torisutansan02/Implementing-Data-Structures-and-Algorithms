def combinations(n, k, version):
    curComb, combs = [], []
    backtrack(1, curComb, combs, n, k, version)
    return combs

def backtrack(i, curComb, combs, n, k, version):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    
    if i > n:
        return
    
    # Standard backtracking algorithm
    if version == "backtrack":
        # Include i in decision tree
        curComb.append(i)
        backtrack(i + 1, curComb, combs, n, k, version)
        curComb.pop()

        # Do not include i in decision tree
        backtrack(i + 1, curComb, combs, n, k, version)
    # Binomial Coefficient C(n, k)
    elif version == "binomial":
        for j in range(i, n + 1):
            curComb.append(j)
            backtrack(j + 1, curComb, combs, n, k, version)
            curComb.pop()

print("\n")

print("Testing with standard backtracking", "\n")

n, k = 5, 2

print(combinations(n, k, "backtrack"), "\n")

print("Testing with binomial coefficient", "\n")

n, k = 5, 2

print(combinations(n, k, "binomial"), "\n")