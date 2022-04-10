class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(1, numRows + 1):
            ret.append([1] * i)
        for r in range(2, len(ret)):
            for c in range(1, len(ret[r]) - 1):
                ret[r][c] = ret[r - 1][c - 1] + ret[r - 1][c]

        return ret
        