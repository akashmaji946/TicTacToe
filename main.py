
board = ['.' for i in range(9)]
# print(board)

board_ = [str(i) for i in range(1, 10)]

turn = 0     # 0 means player A, 1 means player B

get_name_1 = None
get_name_2 = None
get_symbol_1 = None
get_symbol_2 = None
curr_player = None



def board_layout():
  print("The Default Board Layout Is:")
  print(board_[0]+" | "+board_[1]+" | "+board_[2])
  print("-"*9)
  print(board_[3]+" | "+board_[4]+" | "+board_[5])
  print("-"*9)
  print(board_[6]+" | "+board_[7]+" | "+board_[8])

def print_board():
  print(board[0]+" | "+board[1]+" | "+board[2])
  print("-"*9)
  print(board[3]+" | "+board[4]+" | "+board[5])
  print("-"*9)
  print(board[6]+" | "+board[7]+" | "+board[8])

# print(board_layout())
# print(print_board())
def get_turn():
  prompt = "Enter the player number to begin(1/2): "
  try:
   turn_input = int(input(prompt))
   if 1<=turn_input<=2:
     return turn_input
   else:
     return None
  
  except:
    error = "You Entered Wrong Input"
    print(error)
    return None

def validated(next_pos):
  pos = next_pos - 1
  if board[pos] == ".":
    return True
  else:
    return False
  
def get_input_for_turn(t):
  global curr_player
  if t == 0:
    curr_player = get_name_1
  else:
    curr_player = get_name_2
  message = "Enter your next position {0}: ".format(curr_player)
  print(message, end=" ")

  try:
    next_pos = int(input())
    if 1<=next_pos<=9:
      if validated(next_pos):
        return next_pos
      else:
        error = "The position {} is already taken."
        print(error)
        return None
        
    else:
      invalid = "The position is invalid. Try Again."
      print(invalid)
      return None
    

  except:
    error = "The input is not a number:"
    return None

def show_initials():
  print("The players are: ")
  print("Player A: {}".format(get_name_1))
  print("Player B: {}".format(get_name_2))
  print("The symbols chosen are: ")
  print("Player A: {}".format(get_symbol_1))
  print("Player B: {}".format(get_symbol_2))
  print("The current turn: {}".format(curr_player))

def get_current_player(turn):
  if turn == 0:
    curr_player = get_name_1
  else:
    curr_player = get_name_2
  return curr_player


def game_initials():

  global get_name_1, get_name_2, turn, get_symbol_1, get_symbol_2, curr_player

  prompt = "Welcome to the Tic Tac Toe Game:"
  print(prompt)

  message = "This game can be played by two players i.e. A and B"
  print(message)

  get_name_1 = input("Enter player A name: ").upper()
  get_name_2 = input("Enter player B name: ").upper()

  get_symbol_1 = input("Enter player A symbol(O/X): ")
  get_symbol_2 = input("Enter player B symbol(O/X): ")

  t = get_turn()
  while t == None:
    t = get_turn()
  
  turn = t - 1
  curr_player = get_current_player(turn)

  board_layout()
  show_initials()

  # position = get_input_for_turn(turn)
  # while position == None:
  #   position = get_input_for_turn(turn)
  # print(position)
def get_next_position(turn):
  position = get_input_for_turn(turn)
  while position == None:
    position = get_input_for_turn(turn)
  
  return position



  #print(turn)
def set_position(pos, turn):
  if turn == 0:
    board[pos] = get_symbol_1
  else:
    board[pos] = get_symbol_2

def check_winner():
  if board[0]==board[1] and board[1]==board[2] and board[0]!=".":
    return turn
  elif board[3]==board[4] and board[4]==board[5] and board[3]!=".":
    return turn
  elif board[6]==board[7] and board[7]==board[8] and board[6]!=".":
    return turn
  elif board[0]==board[3] and board[0]==board[6] and board[0]!=".":
    return turn
  elif board[1]==board[4] and board[1]==board[7] and board[1]!=".":
    return turn
  elif board[2]==board[5] and board[2]==board[8] and board[2]!=".":
    return turn
  elif board[0]==board[4] and board[0]==board[8] and board[0]!=".":
    return turn
  elif board[2]==board[4] and board[4]==board[6] and board[2]!=".":
    return turn
  else:
    return None

def main():
  global turn
  total_filled = 0
  game_initials()
  while True:
    pos = get_next_position(turn)
    print(pos)
    set_position(pos - 1, turn)
    print_board()
    total_filled += 1

    

    winner = check_winner()
    if winner == 0:
      winner_name = get_current_player(winner)
    elif winner == 1:
      winner_name = get_current_player(winner)
    else:
      turn = 1 - turn
      if total_filled == 9:
        print("Game tied")
        break
      continue
    if winner != None:
      print("Player {} is winner...".format(winner_name))
      break





if __name__ =="__main__":
  main()


