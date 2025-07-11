class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            #if index is the length of word, we have found word
            if i == len(word):
                return True
            #check conditions to make sure letter currently on is valid and expected letter
            if (min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] != word[i]):
                return 
            #word found! add to visit
            visit.add((r, c))
            #variable to store and return a boolean as to if there is a valid word 
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visit.remove((r, c))
            return res

        #iterate throught to find the first letter
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    if dfs(r, c, 0):
                        return True

        return False

        