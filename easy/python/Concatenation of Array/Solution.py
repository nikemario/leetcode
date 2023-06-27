class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list()

        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)

        return ans