from abc import ABC, abstractmethod
from collections import defaultdict, Counter

class AbstractArrayHash(ABC):
    @abstractmethod
    def twoSum(self, nums, target): pass

    @abstractmethod
    def groupAnagrams(self, strs): pass

    @abstractmethod
    def topKFrequent(self, nums, k): pass

    @abstractmethod
    def isAnagram(self, s, t): pass

    @abstractmethod
    def longestConsecutive(self, nums): pass

    @abstractmethod
    def containsDuplicate(self, nums): pass

    @abstractmethod
    def productExceptSelf(self, nums): pass

    @abstractmethod
    def subarraySum(self, nums, k): pass

    @abstractmethod
    def findMaxLength(self, nums): pass

    @abstractmethod
    def intersection(self, nums1, nums2): pass

    @abstractmethod
    def longestSubstringWithoutRepeating(self, s): pass

    @abstractmethod
    def minimumWindowSubstring(self, s, t): pass

    @abstractmethod
    def threeSum(self, nums): pass

class ArrayHashProblems(AbstractArrayHash):
    def twoSum(self, nums, target):
        map1 = {}
        for i, n in enumerate(nums):
            if target - n in map1:
                return [map1[target - n], i]
            map1[n] = i

    def groupAnagrams(self, strs):
        map1 = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            map1[key].append(word)
        return list(map1.values())

    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = [[] for i in range(len(nums))]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n - 1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

    def subarraySum(self, nums, k):
        prefixSum = {0: 1}
        total = 0
        currSum = 0
        for n in nums:
            currSum += n
            total += prefixSum.get(currSum - k, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return total

    def findMaxLength(self, nums):
        count = 0
        map1 = {0: -1}
        maxLength = 0
        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count in map1:
                maxLength = max(maxLength, i - map1[count])
            else:
                map1[count] = i
        return maxLength

    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def longestSubstringWithoutRepeating(self, s):
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    def minimumWindowSubstring(self, s, t):
        if not t or not s:
            return ""

        countT = Counter(t)
        window = {}

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""

    def threeSum(self, nums):
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
