def checkmate(board):

    if not board:
        print("Error!!")
        return

    try:
        empty_lines = board.splitlines()
        rows = [line.strip() for line in empty_lines if line.strip()]
    except:
        print("Error!!")
        return
    if not rows:
        print("Error!!")
        return

    size = len(rows)
    valid_chars = {'K', 'Q', 'B', 'R', 'P', '.'}
    K_pos = None
    count_K = 0

    for r, row in enumerate(rows):
        if len(row) != size:
            print("Error!!")
            return

        for c, char in enumerate(row):
            if char not in valid_chars:
                print("Error!!")
                return
            
            if char == 'K':
                K_pos = (r, c)
                count_K += 1

    if count_K != 1:
        print("Error!!")
        return

    class pieces:
        def __init__(self):
            self.addr = []
            self.atk = []

    rook = pieces()
    bishop = pieces()
    queen = pieces()
    pawn = pieces()
    king = pieces()

    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == "R": 
                rook.addr.append([r,c])
            elif cell == "B": 
                bishop.addr.append([r,c])
            elif cell == "P": 
                pawn.addr.append([r,c])
            elif cell == "Q": 
                queen.addr.append([r,c])
            elif cell == "K": 
                king.addr.append([r,c])
    #rook queen  
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            for r_rook, c_rook in rook.addr:
                if r == r_rook or c == c_rook:
                    rook.atk.append([r,c])

            for r_queen, c_queen in queen.addr:
                if r == r_queen or c == c_queen:
                    queen.atk.append([r,c])
       
    #bishop queen
    for i in range(1,len(rows)+1):
        for r, c in bishop.addr:
            bishop.atk.append([r + i, c + i])
            bishop.atk.append([r - i, c - i])
            bishop.atk.append([r + i, c - i])
            bishop.atk.append([r - i, c + i])
        for r, c in queen.addr:
            queen.atk.append([r + i, c + i])
            queen.atk.append([r - i, c - i])
            queen.atk.append([r + i, c - i])
            queen.atk.append([r - i, c + i])

    #pawn
    for r, c in pawn.addr:
        pawn.atk.append([r - 1, c - 1])
        pawn.atk.append([r - 1, c + 1])
    # print("PAWN",pawn.addr)
    # print(pawn.atk)
    # print("BISHOP",bishop.addr)
    # print(bishop.atk)
    # print("ROOK",rook.addr)
    # print(rook.atk)
    # print("QUEEN",queen.addr)
    # print(queen.atk)
    # print("KING",king.addr)

    if king.addr[0] in pawn.atk or king.addr[0] in bishop.atk or king.addr[0] in rook.atk or king.addr[0] in queen.atk:
        print("Success")
        return
    else: print("Fail")