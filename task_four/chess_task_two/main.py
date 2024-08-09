import pygame

print(pygame.ver)


pygame.init()

WIDTH = 900
HIGHT = 800

screen = pygame.display.set_mode([WIDTH, HIGHT])

timer = pygame.time.Clock()
fps = 60


# game variables :

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen','bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                  (0,1),(1,1),(1,2),(3,1),(4,1),(5,1),(6,1),(7,1)]


black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen','bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                  (0,6),(1,6),(1,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100

valid_moves = []
# game images
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))

black_king = pygame.image.load('images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))

black_rook = pygame.image.load('images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))

black_bishop = pygame.image.load('images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))

black_knight = pygame.image.load('images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))

black_pawn = pygame.image.load('images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))

white_queen = pygame.image.load('images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))

white_king = pygame.image.load('images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))

white_rook = pygame.image.load('images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))

white_bishop = pygame.image.load('images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))

white_knight = pygame.image.load('images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))

white_pawn = pygame.image.load('images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

piece_list = ['pawn','queen','king','knight','rook', 'bishop']
            
# check_variables
# making the board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0 :
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])  # Find the index of the current piece

        # Check which piece we are drawing
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))     

        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                    100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])  # Find the index of the current piece

        # Check which piece we are drawing
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))     
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step > 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                    100, 100], 2)
                

# check options 

# def check_options(pieces, locations, turn):
#     moves_list = []
#     all_moves_list = []
#     for i in range((pieces)):
#         location = locations[i]
#     piece = pieces[i]
#     # if piece == 'pawn':
#     #     moves_list = ckeck_pawn(location, turn)
#     # elif piece == 'rook':
#     #     moves_list  = check_rook(location, turn)
#     # elif piece == 'knight':
#     #     moves_list  = check_knight(location, turn)
#     # elif piece == 'knight':
#     #     moves_list  = check_bishop(location, turn)
#     # elif piece == 'queen':
#     #     moves_list  = check_queen(location, turn)
#     # elif piece == 'king':
#     #     moves_list  = check_king(location, turn)
#     all_moves_list.append(moves_list)
#     return all_moves_list

def valid_pawn_moves(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else: # for black pawns
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# white_options = check_options(white_pieces, white_locations, "white") 
# black_options = check_options(black_pieces, black_locations, "black") 

run = True

while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    # get actions of keyboard ...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fun = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coord in white_locations:
                    selection = white_locations.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    white_locations[selection] = click_coord
                    if click_coord in black_locations:
                        black_piece = black_locations.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    else:
                        # black_options = check_options(black_pieces, black_locations, "black")        
                        # white_options = check_options(white_pieces, white_locations, "white") 
                        # turn_step= 2
                        selection = 100
                        valid_moves = []  

            # for black
            if turn_step > 1:
                if click_coord in black_locations:
                    selection = black_locations.index(click_coord)
                    if turn_step == 3:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    black_locations[selection] = click_coord
                    if click_coord in white_locations:
                        white_piece = white_locations.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    else:
                        # white_options = check_options(white_pieces, white_locations, "white") 
                        # black_options = check_options(black_pieces, black_locations, "black")        
                        turn_step= 2
                        selection = 100
                        valid_moves = []       

    pygame.display.flip()        
pygame.quit()


