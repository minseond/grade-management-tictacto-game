import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # 가로, 세로, 대각선 방향2으로 승자 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def player_move(board):
    while True:
        try:
            row = int(input("행을 선택하세요 (1, 2, 3): ")) - 1
            col = int(input("열을 선택하세요 (1, 2, 3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("해당 위치는 이미 선택되었습니다. 다른 위치를 선택하세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 다시 입력하세요.")

def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("틱택토 게임을 시작합니다!")

    while True:
        print_board(board)
        player_move(board)
        if check_winner(board):
            print_board(board)
            print("축하합니다! 플레이어가 이겼습니다!")
            break
        if is_board_full(board):
            print_board(board)
            print("무승부입니다!")
            break

        print("컴퓨터가 생각 중입니다...")
        computer_move(board)
        if check_winner(board):
            print_board(board)
            print("컴퓨터가 이겼습니다! 다음에 다시 도전하세요!")
            break
        if is_board_full(board):
            print_board(board)
            print("무승부입니다!")
            break

if __name__ == "__main__":
    main()
