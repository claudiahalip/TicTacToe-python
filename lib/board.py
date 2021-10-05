class Board:
    board = {
        1 : ' ', 2 : ' ', 3 : ' ',
        4 : ' ', 5 : ' ', 6 : ' ',
        7 : ' ', 8 : ' ', 9 : ' '
    }
    
    def display_board():
        print(Board.board[1] + '  | ' + Board.board[2] + ' | ' + Board.board[3])
        print('-----------') 
        print(Board.board[4] + '  | ' + Board.board[5] + ' | ' + Board.board[6])
        print('-----------') 
        print(Board.board[7] + '  | ' + Board.board[8] + ' | ' + Board.board[9])
        
        