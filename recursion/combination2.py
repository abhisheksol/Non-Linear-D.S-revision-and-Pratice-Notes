class Solution:

    def findCombinations(self, ind, arr, target, ans, ds):
        if target == 0:
            ans.append(ds[:])
            return

        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue

            if arr[i] > target:
                break

            ds.append(arr[i])
            self.findCombinations(i+1, arr, target-arr[i], ans, ds)
            ds.pop() #bt

    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()
        self.findCombinations(0, candidates, target, ans, [])
        return ans

# Example Usage
sol = Solution()
candidates = [1,1,1,2,2]
target = 4
result = sol.combinationSum2(candidates, target)
print(result)
