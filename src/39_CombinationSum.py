class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.helper(sorted(candidates), target)

    def helper(self, candidates, target):
        if (not candidates) or (candidates[0] > target):
            return []
        if candidates[0] == target:
            return [[candidates[0]]]

        # first scenario, use the 0th candidate
        res = self.helper(candidates, target - candidates[0])
        res = [[candidates[0]] + each for each in res]

        # second scenario, donot use the 0th candidate
        res += self.helper(candidates[1:], target)

        return res



#print [[1] + i for i in [[2], [3], [4]]] + [[123], [321]]
sol = Solution()
candidates = [2, 3 ,6 ,7]
target = 7
print sol.combinationSum(candidates, target)
        

