class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, open, close):
            if len(path) == 2 * n:
                res.append(path[:])
                return 

            if open < n:
                backtrack(path + '(', open + 1, close)
            if close < open:
                backtrack(path + ')', open, close + 1)

        res = []
        backtrack("", 0, 0)
        return res
        