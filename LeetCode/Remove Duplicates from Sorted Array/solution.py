from typing import List
from collections import OrderedDict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNumsDict = OrderedDict.fromkeys(nums)
        uniqueNumsList = list(uniqueNumsDict.keys())
        k = len(uniqueNumsList)
        nums[:k] = uniqueNumsList
        return k
