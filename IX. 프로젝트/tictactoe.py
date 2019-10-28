class TicTacToe:
    def __init__(self):
        self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
        self.current_turn = "X"

    def set(self, row, col):
        if self.get(row, col) == ".":   # 말은 빈 칸에만 놓을 수 있음
            self.current_turn = "X" if self.current_turn == "O" else "O"
            self.board[(row * 3) + col] = self.current_turn

    def get(self, row, col):
        return self.board[(row * 3) + col]

    def check_winner(self):
        check = self.current_turn
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check:
                # 세로 |
                return check
            elif self.get(0, i) == self.get(1, i) == self.get(2, i) == check:
                # 가로 -
                return check
            
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check:
            # 대각선 역슬래시
            return check
        elif self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check:
            # 대각선 /
            return check
        
        if not "." in self.board:   # 점이 없다 -> 판이 다 채워짐
            # 무승부
            return "d"  

    def __str__(self):
        s = ""
        for i, v in enumerate(self.board):
            s += v
            if i % 3 == 2:
                s += "\n"
        return s