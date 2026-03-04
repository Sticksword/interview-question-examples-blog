import numpy as np

class Solution:
    def solve(self, matrix):
        bestSoFar = []
        for idx, row in enumerate(matrix):
            if idx == 0:
                bestSoFar.append(self.processRow(row))
            elif idx == 1:
                bestSoFar.append(np.maximum(bestSoFar[0], self.processRow(row)))
            else:
                ifWePickThisRow = np.add(bestSoFar[idx - 2], self.processRow(row))
                bestSoFar.append(np.maximum(bestSoFar[idx - 1], ifWePickThisRow))
        
        print(bestSoFar)
        return max(bestSoFar[-1])

    def processRow(self, row):
        solution = [row[0], row[1]]
        for rowIdx in range(2, len(row)):
            c = max(row[rowIdx] + solution[rowIdx - 2], solution[rowIdx - 1])
            solution.append(c)
        return solution


matrix_test_1 = [
    [1, 7, 6, 5],
    [9, 9, 3, 1],
    [4, 8, 1, 2]
]

s = Solution()
print(s.solve(matrix_test_1) == 22)

matrix_test_2 = [
    [1, 7, 6, 5],
    [9, 9, 3, 1],
]

print(s.solve(matrix_test_2))

matrix_test_3 = [
    [1, 7, 6, 5],
    [9, 9, 3, 1],
    [4, 8, 1, 2],
    [9, 9, 1, 1]
]

print(s.solve(matrix_test_3))
