import time

def checkWin(board, char):
	# Top row (1-2-3)
	if board[0][0] == char and board[0][1] == char and board[0][2] == char:
		return True
	# Middle row (4-5-6)
	elif board[1][0] == char and board[1][1] == char and board[1][2] == char:
		return True
	# Bottom row (7-8-9)
	elif board[2][0] == char and board[2][1] == char and board[2][2] == char:
		return True
	# Left column (1-4-7)
	elif board[0][0] == char and board[1][0] == char and board[2][0] == char:
		return True
	# Middle column (2-5-8)
	elif board[0][1] == char and board[1][1] == char and board[2][1] == char:
		return True
	# Right column (3-6-9
	elif board[0][2] == char and board[1][2] == char and board[2][2] == char:
		return True
	# Positive slope diagonal (3-5-7)
	elif board[0][2] == char and board[1][1] == char and board[2][0] == char:
		return True
	# Negative slope diagonal (1-5-9)
	elif board[0][0] == char and board[1][1] == char and board[2][2] == char:
		return True
	else:
		return False

def catWin(board):
	for row in range(3):
		for column in range(3):
			if board[row][column] == "X" or board[row][column] == "O":
				continue
			if board[row][column] > 0 and board[row][column] < 10:
				return False

	return True	


print("\n-=+ Tic Tac Toe by @thompmatt +=-\n")
time.sleep(2)
print("Welcome to Tic Tac Toe!")
time.sleep(2)
print("The rules are simple: align three \"X\" or \"O\" in a straight or diagonal line to win!\n")
time.sleep(3)

board = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
P1 = True
run = True
cat = False

while run:
	print("___________________________________________________________________________________\n")

	for row in board:
		for column in row:
			print(column, end="  ")
		print()

	if checkWin(board, "X"):
			run = False
			break
	elif checkWin(board, "O"):
			run = False
			break	
	elif catWin(board):
			cat = True
			run = False
			break

	if P1:
		print("\nP1 (X), your turn: ")
		validChoice = False

		while not validChoice:
			choice = input()

			if not choice.isdigit():
				print("Invalid input. Please enter a # (1-9) available on the board.")
			elif int(choice) > 0 and int(choice) < 10:
				for row in range(3):
					for column in range(3):
						if board[row][column] == int(choice):
							validChoice = True
							board[row][column] = "X"

				if not validChoice:
					print("Invalid input. Please enter a # (1-9) available on the board.")
			else:
				print("Invalid input. Please enter a # (1-9) available on the board.")

		P1 = False
		print()

	else:
		print("\nP2 (0), your turn: ")
		validChoice = False

		while not validChoice:
			choice = input()

			if not choice.isdigit():
				print("Invalid input. Please enter a # (1-9) available on the board.")
			elif int(choice) > 0 and int(choice) < 10:
				for row in range(3):
					for column in range(3):
						if board[row][column] == int(choice):
							validChoice = True
							board[row][column] = "O"

				if not validChoice:
					print("Invalid input. Please enter a # (1-9) available on the board.")
			else:
				print("Invalid input. Please enter a # (1-9) available on the board.")
		
		P1 = True
		print()

time.sleep(1)
if cat:
	print("\nThe cat has won!\nBetter luck next time! Thanks for playing!\n")
elif not P1:
	print("\nPlayer 1 has won!\nThanks for playing!\n")
else:
	print("\nPlayer 2 has won!\nThanks for playing!\n")