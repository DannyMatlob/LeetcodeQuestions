def solution(rows, cols, black):
    black_set = set(tuple(arr) for arr in black)
    for arr in black_set:
        print(f"{arr[0]},{arr[1]}")
        
    solutions = [0] * 5
    for i in range(rows-1):
        for j in range(cols-1):
            black_count = 0
            coord1 = (i, j)
            coord2 = (i+1, j)
            coord3 = (i, j+1)
            coord4 = (i+1, j+1)
            if coord1 in black_set:
                black_count += 1
            if coord2 in black_set:
                black_count += 1
            if coord3 in black_set:
                black_count += 1
            if coord4 in black_set:
                black_count += 1
            solutions[black_count] += 1
    return solutions

def make_list(i, j):
    return [i, j]

class Main:
    def __init__(self):
        pass

    def run(self):
        rows = 4
        cols = 4
        black = [[0, 1], [2, 2], [3, 3]]
        solutions = solution(rows, cols, black)
        print(solutions)

if __name__ == '__main__':
    main = Main()
    main.run()

"""
For a grid of black and white cells with rows rows and cols columns, you're given an array black that contains the [row, column] coordinates of all the black cells in the grid.

Your task is to compute how many 2 × 2 submatrices of the grid contain exactly blackCount black cells, for each 0 ≤ blackCount ≤ 4. As a result, you will return an array of 5 integers, where the ith element is the number of 2 × 2 submatrices with exactly i black cells.

It is guaranteed that black cell coordinates in the black array are pairwise unique, so the same cell is not colored twice.

Example

For rows = 3, cols = 3, and black = [[0, 0], [0, 1], [1, 0]], the output should be solution(rows, cols, black) = [1, 2, 0, 1, 0].

Expand to see the example video.

Note: If you are not able to see the video, use this link to access it.

Initially, result = [0, 0, 0, 0, 0].
The 2 × 2 submatrix with the upper-left corner at (0, 0) contains 3 black cells. result = [0, 0, 0, 1, 0].
The 2 × 2 submatrix with the upper-left corner at (0, 1) contains 1 black cell. result = [0, 1, 0, 1, 0].
The 2 × 2 submatrix with the upper-left corner at (1, 0) contains 1 black cell. result = [0, 2, 0, 1, 0].
The 2 × 2 submatrix with the upper-left corner at (1, 1) contains 0 black cells. result = [1, 2, 0, 1, 0]
"""
