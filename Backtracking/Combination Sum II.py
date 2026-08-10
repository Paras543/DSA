class Solution(object):
    def backtrack(self, candidates, i, combination, ans, target, start):

        if target == 0:
            ans.append(combination[:])
            return

        if i == len(candidates) or target < 0:
            return

        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            combination.append(candidates[i])

            self.backtrack(
                candidates,
                i + 1,
                combination,
                ans,
                target - candidates[i],
                i + 1
            )

            combination.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()

        combination = []
        ans = []

        self.backtrack(
            candidates,
            0,
            combination,
            ans,
            target,
            0
        )

        return ans

        