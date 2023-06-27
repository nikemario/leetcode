class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        ans = list()

        for x in range(n):
            ans.append(nums[x])
            ans.append(nums[x+n])

        return ans