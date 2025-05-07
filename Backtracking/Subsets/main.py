def subsets(nums, duplicates):
    # Sort the list if there are duplicates
    if duplicates:
        nums.sort()
    
    # Subsets contains all subsets
    # Curset contains the current set in the decision tree
    subsets, curSet = [], []

    # Call the helper function at i = 0
    helper(0, nums, curSet, subsets, duplicates)
    
    # Return the subsets
    return subsets


def helper(i, nums, curSet, subsets, duplicates):
    # Leaf of the decision tree
    if i == len(nums):
        # Append a copy of the current set
        subsets.append(curSet.copy())
        return

    # Include nums[i] in the decision tree
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets, duplicates)
    curSet.pop()

    # If there are duplicates, skip repeated values
    if duplicates:
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

    # Do not include nums[i] in the decision tree
    helper(i + 1, nums, curSet, subsets, duplicates)

print("\n")

nums = [1, 2, 3]
duplicates = False

print("Testing Without Duplicates", "\n")

print(subsets(nums, duplicates), "\n")

nums = [1, 2, 2, 3]
duplicates = True

print("Testing With Duplicates", "\n")

print(subsets(nums, duplicates), "\n")