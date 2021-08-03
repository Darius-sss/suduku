import csv

class Solution:

    def load_problem(self, curr):    # 加载问题数据 curr = self.curr
        with open(file=r'./ziyuan/problem.txt', mode='r', encoding='utf-8') as fr:
            data = list(csv.reader(fr))
        return [[data[curr][i * 9 + j] for j in range(9)] for i in range(9)]

    def solveSudoku(self, board) -> None:
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return

        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] != "0":
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        while True:
            modified = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == "0":
                        mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):
                            digit = bin(mask).count("0") - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            modified = True
            if not modified:
                break

        for i in range(9):
            for j in range(9):
                if board[i][j] == "0":
                    spaces.append((i, j))
        dfs(0)
        return board


if __name__ == '__main__':
    App = Solution()
    for n in range(1, 11):
        data = App.load_problem(n)
        print(App.solveSudoku(data))
