class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        return self.helper(sorted(candidates), target, 0)

    def helper(self, candidates, target, i):
        if target == 0:
            return [[]]

        n = len(candidates)
        res = []

        while i < n:
            if candidates[i] <= target:
                temp = self.helper(candidates, target - candidates[i], i + 1)
                res += [[candidates[i]] + each for each in temp]
                i += 1

                # avoid duplicate...
                while (i < n) and (candidates[i] == candidates[i - 1]):
                    i += 1
            else:
                break;

        return res



#print [[1] + i for i in [[2], [3], [4]]] + [[123], [321]]
sol = Solution()
#candidates = [23,32,22,19,29,15,11,26,28,20,34,5,34,7,28,33,30,30,16,33,8,15,28,26,17,10,25,12,6,17,30,16,6,10,23,22,20,29,14,5,6,5,5,6,29,20,34,24,16,7,22,11,17,7,33,21,13,15,29,6,19,16,10,21,21,28,8,6]
candidates = [1,1]
target = 2
print sol.combinationSum2(candidates, target)
        

