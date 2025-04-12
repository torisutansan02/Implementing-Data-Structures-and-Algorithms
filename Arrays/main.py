from arrays import ArrayHashProblems

ahp = ArrayHashProblems()

# === Test Cases ===
print("Two Sum:", ahp.twoSum([2, 7, 11, 15], 9))
print("Group Anagrams:", ahp.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print("Top K Frequent:", ahp.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print("Is Anagram:", ahp.isAnagram("anagram", "nagaram"))
print("Longest Consecutive:", ahp.longestConsecutive([100, 4, 200, 1, 3, 2]))
print("Contains Duplicate:", ahp.containsDuplicate([1, 2, 3, 1]))
print("Product Except Self:", ahp.productExceptSelf([1, 2, 3, 4]))
print("Subarray Sum Equals K:", ahp.subarraySum([1, 1, 1], 2))
print("Find Max Length:", ahp.findMaxLength([0, 1]))
print("Intersection:", ahp.intersection([1, 2, 2, 1], [2, 2]))
print("Longest Substring Without Repeating:", ahp.longestSubstringWithoutRepeating("abcabcbb"))
print("Minimum Window Substring:", ahp.minimumWindowSubstring("ADOBECODEBANC", "ABC"))
print("Three Sum:", ahp.threeSum([-1, 0, 1, 2, -1, -4]))
