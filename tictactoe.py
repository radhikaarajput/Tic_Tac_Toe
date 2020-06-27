#board
#display board
#fn to play game
#fn check win
#fn check tie
#check tie
#check win---> check row,check col, check diag


#global variables
game_still_going=True      #default true so that game can start

winner= None

#whose turn
current_player="X"

#simple list 
board=["-","-","-",
      "-","-","-",
      "-","-","-"]

# #fn to play game---> Play game
def play_game():

  #display board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if game is over or not
    check_if_game_over()

    # Flip to the other player
    flip_player()
    # Since the game is over, print the winner or tie
  
  if winner == "X" or winner == "O":
      print(winner + " WON !!!")
  if winner == None:
      print("  !! Tie  !!")



#fn to display board
def display_board():
  print(board[0]+'|' +board[1]+'|'+ board[2]+'|')
  print(board[3]+'|' +board[4]+'|'+ board[5]+'|')
  print(board[6]+'|' +board[7]+'|'+ board[8]+'|')




def handle_turn(player):
    
  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()


#check win---> check row,check col, check diag
def check_if_win():
  #set global var
  global winner

  #check rows
  row_winner=check_row()
  col_winner=check_col()
  diag_winner=check_diagonal()

  if row_winner:
    winner=row_winner
  elif col_winner:
    winner=col_winner
  elif diag_winner:
    winner=check_diagonal()
  else:
    winner=None
  return

def check_row():
  global game_still_going

  #same value true then row win if wi1 has wiining configuration
  row_1 = board[0]== board[1]==board[2] != "-"      
  row_2 = board[3]== board[4]==board[5] != "-"
  row_3 = board[6]== board[7]==board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going=False

#check who won among rows
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]

  return


def check_col():
  global game_still_going
  col_1 = board[0]== board[3]==board[6] != "-"      
  col_2 = board[1]== board[4]==board[7] != "-"
  col_3 = board[2]== board[5]==board[8] != "-"

  if col_1 or col_2 or col_3:
    game_still_going=False

    #check who won among cols
  if col_1:
    return board[0]
  if col_2:
    return board[1]
  if col_3:
    return board[2]
  return



def check_diagonal():
  global game_still_going
  diagonal_1 = board[0]== board[4]==board[8] != "-"      
  diagonal_2 = board[6]== board[4]==board[2] != "-"
  

  if diagonal_1 or diagonal_2:
    game_still_going=False

#check who won among cols
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[6]
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False
    return True
  else:
    return False



#flip to whose turn x's turn flip=== y's turn flip, again x's turn flip
def flip_player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"

play_game()