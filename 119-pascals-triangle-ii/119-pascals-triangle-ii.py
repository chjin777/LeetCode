class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        for i in range(1, rowIndex + 2):
            ret.append([1] * i)
        for r in range(2, len(ret)):
            for c in range(1, len(ret[r]) - 1):
                ret[r][c] = ret[r - 1][c - 1] + ret[r - 1][c]

        return ret[rowIndex]