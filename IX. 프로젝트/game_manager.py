from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        # 게임 판 보여주기
        print(self.ttt)
        while True:
            # row, col 입력 받기
            row = int(input("row : "))
            col = int(input("col : "))
            self.ttt.set(row, col)
            print(self.ttt)
            # check_winnier이면 끝
            if  self.ttt.check_winner() == "O":
                print("O win !")
                break
            elif self.ttt.check_winner() == "X":
                print("X win !")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

if __name__ == '__main__':
    gm = GameManager()
    gm.play()