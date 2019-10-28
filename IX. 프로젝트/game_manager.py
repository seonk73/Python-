from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        # 게임 판 보여주기
        print(self.ttt)
        # row, col 입력 받기
        self.ttt.set(1, 1)
        print(self.ttt)
        # check_winnier이면 끝

if __name__ == '__main__':
    gm = GameManager()
    gm.play()