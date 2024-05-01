import socket
import threading

# set starting details to make connection and decode messages
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnected"
SERVER = '172.16.22.27' # set server to IP address provided by server when server is started
ADDR = (SERVER, PORT)

# start and bind client socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


class Game:
    # class for tic-tac-toe game
    def __init__(self):
        self.positions = [x for x in range(1, 10)]
    
    # sets the client's symbol to X or O, received from server
    def set_symbol(self, symbol):
        self.symbol = symbol
    
    # sets who goes first, received from server
    def set_turn(self, turn):
        if turn == '0':
            self.turn = False
        elif turn == '1':
            self.turn = True

    # if it is your turn, do the turn
    def run_game(self):
        if self.turn == True:
            self.show_board()
            self.get_user_input()

    # receive message from server from other client, update board with their position
    def receive_user_input(self, spot):
        if spot[0] in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if self.symbol == 'X':
                self.update_board(int(spot) - 1, 'O')
            else:
                self.update_board(int(spot) - 1, 'X')
            self.turn = True
            self.run_game()
        else:
            if self.symbol == 'X':
                self.update_board(int(spot[1]) - 1, 'O')
            else:
                self.update_board(int(spot[1]) - 1, 'X')
            self.show_board()
            if spot[0] == 'L':
                self.check_winner(msg='You lose!')
            if spot[0] == 'T':
                self.end_tie()

    # pass the spot you chose to the server to send to the other client
    def pass_user_input(self, spot):
        send(spot)
        self.turn = False
    
    # check to see if you won or lost, sets symbol colors
    def check_winner(self, spot=None, msg=None):
        won = False
        p = self.positions
        for i in range(len(p)):
            if p[i] == '\033[1;33;40mX':
                p[i] = 'X'
            elif p[i] == '\033[1;34;40mO':
                p[i] = 'O'
        for i in ['X', 'O']:
            if p[0] == i and p[1] == i and p[2] == i:
                if i == self.symbol:
                    self.positions[0] = f'\033[1;32;40m{i}'
                    self.positions[1] = f'\033[1;32;40m{i}'
                    self.positions[2] = f'\033[1;32;40m{i}'
                else:
                    self.positions[1] = f'\033[1;31;40m{i}'
                    self.positions[2] = f'\033[1;31;40m{i}'
                    self.positions[0] = f'\033[1;31;40m{i}'
                won = True
            elif p[0] == i and p[3] == i and p[6] == i:
                if i == self.symbol:
                    p[0] = f'\033[1;32;40m{i}'
                    p[3] = f'\033[1;32;40m{i}'
                    p[6] = f'\033[1;32;40m{i}'
                else:
                    p[0] = f'\033[1;31;40m{i}'
                    p[3] = f'\033[1;31;40m{i}'
                    p[6] = f'\033[1;31;40m{i}'
                won = True
            elif p[0] == i and p[4] == i and p[8] == i:
                if i == self.symbol:
                    self.positions[0] = f'\033[1;32;40m{i}'
                    self.positions[4] = f'\033[1;32;40m{i}'
                    self.positions[8] = f'\033[1;32;40m{i}'
                else:
                    self.positions[0] = f'\033[1;31;40m{i}'
                    self.positions[4] = f'\033[1;31;40m{i}'
                    self.positions[8] = f'\033[1;31;40m{i}'
                won = True
            elif p[8] == i and p[7] == i and p[6] == i:
                if i == self.symbol:
                    self.positions[8] = f'\033[1;32;40m{i}'
                    self.positions[7] = f'\033[1;32;40m{i}'
                    self.positions[6] = f'\033[1;32;40m{i}'
                else:
                    self.positions[8] = f'\033[1;31;40m{i}'
                    self.positions[7] = f'\033[1;31;40m{i}'
                    self.positions[6] = f'\033[1;31;40m{i}'
                won = True
            elif p[8] == i and p[5] == i and p[2] == i:
                if i == self.symbol:
                    self.positions[8] = f'\033[1;32;40m{i}'
                    self.positions[5] = f'\033[1;32;40m{i}'
                    self.positions[2] = f'\033[1;32;40m{i}'
                else:
                    self.positions[8] = f'\033[1;31;40m{i}'
                    self.positions[5] = f'\033[1;31;40m{i}'
                    self.positions[2] = f'\033[1;31;40m{i}'
                won = True
            elif p[2] == i and p[4] == i and p[6] == i:
                if i == self.symbol:
                    self.positions[2] = f'\033[1;32;40m{i}'
                    self.positions[4] = f'\033[1;32;40m{i}'
                    self.positions[6] = f'\033[1;32;40m{i}'
                else:
                    self.positions[2] = f'\033[1;31;40m{i}'
                    self.positions[4] = f'\033[1;31;40m{i}'
                    self.positions[6] = f'\033[1;31;40m{i}'
                won = True
            elif p[1] == i and p[4] == i and p[7] == i:
                if i == self.symbol:
                    self.positions[1] = f'\033[1;32;40m{i}'
                    self.positions[4] = f'\033[1;32;40m{i}'
                    self.positions[7] = f'\033[1;32;40m{i}'
                else:
                    self.positions[1] = f'\033[1;31;40m{i}'
                    self.positions[4] = f'\033[1;31;40m{i}'
                    self.positions[7] = f'\033[1;31;40m{i}'
                won = True
            elif p[3] == i and p[4] == i and p[5] == i:
                if i == self.symbol:
                    self.positions[3] = f'\033[1;32;40m{i}'
                    self.positions[4] = f'\033[1;32;40m{i}'
                    self.positions[5] = f'\033[1;32;40m{i}'
                else:
                    self.positions[3] = f'\033[1;31;40m{i}'
                    self.positions[4] = f'\033[1;31;40m{i}'
                    self.positions[5] = f'\033[1;31;40m{i}'
                won = True
            if won:
                if spot is not None:
                    send(f'L{spot}')
                self.show_board()
                self.end_win(msg)
    
    # check to see if it was a tie
    def check_tie(self, spot):
        count = 0
        for i in self.positions:
            try:
                int(i)
            except:
                count += 1
        if count == 9:
            send(f'T{spot}')
            self.end_tie()

    # prints the current board
    def show_board(self):
        for i in range(len(self.positions)):
            # sets symbol colors
            if self.positions[i] == 'X':
                self.positions[i] = '\033[1;33;40mX'
            elif self.positions[i] == 'O':
                self.positions[i] = '\033[1;34;40mO'
        print(f'\n \033[1;37;40m{self.positions[0]} \u001b[0m| \033[1;37;40m{self.positions[1]} \u001b[0m| \033[1;37;40m{self.positions[2]} ')
        print('\u001b[0m---+---+---')
        print(f' \033[1;37;40m{self.positions[3]} \u001b[0m| \033[1;37;40m{self.positions[4]} \u001b[0m| \033[1;37;40m{self.positions[5]} ')
        print('\u001b[0m---+---+---')
        print(f' \033[1;37;40m{self.positions[6]} \u001b[0m| \033[1;37;40m{self.positions[7]} \u001b[0m| \033[1;37;40m{self.positions[8]} \n\u001b[0m')

    # updates the board based on user input, or message received from other client
    def update_board(self, spot, opponent_symbol=None):
        if opponent_symbol is not None:
            self.positions[spot] = opponent_symbol
        else:
            self.positions[spot] = self.symbol

    # gets client's input when it is their turn
    def get_user_input(self):
        finished = False
        while not finished:
            try:
                spot = int(input('Where would you like to go? '))
                if spot > 9 or spot < 1 or self.positions[spot - 1] not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    print('Not a valid number!')
                else:
                    self.update_board(spot - 1)
                    self.show_board()
                    finished = True
            except:
                print('Not a valid number!')
        self.check_winner(str(spot))
        self.check_tie(str(spot))
        self.pass_user_input(str(spot))
    
    # function that displays end message if there is a winner/loser
    def end_win(self, msg=None):
        if msg is not None:
            print(f'\n{msg}')
        else:
            print('You win!')
        send(DISCONNECT_MESSAGE)
        quit()
    
    # function that displays end message if it was a tie
    def end_tie(self):
        print('\nIt was a tie!')
        send(DISCONNECT_MESSAGE)
        quit()

# starts the game
def start_game(game):
    game.run_game()

# sends the location and win/lose/tie condition if applicable after client enters input
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

# receives input from other client through server, sends to game's receive_user_input function
def receive():
    count = 0
    game = Game()
    while True:
        if count != 0:
            print('Waiting for opponent...')
        msg = client.recv(HEADER).decode(FORMAT)
        if msg:
            if count != 0:
                game.receive_user_input(msg)
            else:
                game.set_symbol(msg[0])
                game.set_turn(msg[1])
                start_game(game)
                count += 1

# create and start thread
t = threading.Thread(target=receive)
t.start()