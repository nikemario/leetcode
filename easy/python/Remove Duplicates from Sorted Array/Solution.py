class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if num in ans:
                print("exists")
            else:
                ans.append(num)
        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)