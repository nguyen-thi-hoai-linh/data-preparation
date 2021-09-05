import numpy as np
board = np.zeros(9, dtype=int)

def check_win():
    if any(np.sum(board.reshape(3, 3), 1) == 3) or any(np.sum(board.reshape(3, 3), 0) == 3) or sum(np.diag(board.reshape(3, 3))) == 3 or sum(np.diag(board.reshape(3, 3)[::-1])) == 3:
        return True
    if any(np.sum(board.reshape(3, 3), 1) == -3) or any(np.sum(board.reshape(3, 3), 0) == -3) or sum(np.diag(board.reshape(3, 3))) == -3 or sum(np.diag(board.reshape(3, 3)[::-1])) == -3:
        return True
    return False

def play_turn():
    board_list = []
    if turn==1:
        x = int(input(f"nguoi choi A chon vi tri tu 0->8:"))
    else:
        x = int(input(f"nguoi choi thu B chon vi tri tu 0->8:"))
    try:
        if board[x] == 0:
            board[x] = turn
        else:
            play_turn()
    except IndexError:
        play_turn()
    for i in range(0, 9):
        if board[i] == -1:
            board_list.append('O')
        elif board[i] == 1:
            board_list.append('X')
        elif board[i] == 0:
            board_list.append(' ')
    print("""
 {} | {} | {}
---+---+---
 {} | {} | {}
---+---+---
 {} | {} | {}
""".format(*board_list))


turn = 1
move = 9
while move > 0:
    play_turn()
    if check_win():
        if turn ==1:
          print("Player A has won!")
        else:
            print("Player B has won")
        break
    turn = turn * -1
    move = move - 1
    if move==0:
      print("draw")
