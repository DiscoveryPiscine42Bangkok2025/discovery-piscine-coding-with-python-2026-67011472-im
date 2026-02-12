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

    def inboard(r, c): # เช็คขอบ board
        return 0 <= r < size and 0 <= c < size
    
    #rook
    for r, c in rook.addr:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            while inboard(nr,nc):
                if rows[nr][nc] == 'K': # เจอ King
                    print("Success")
                    return
                if rows[nr][nc] != '.': # เจอหมากขวาง
                    break
                nr += dr
                nc += dc
       
    #bishop
    for r, c in bishop.addr:
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            while inboard(nr, nc):
                if rows[nr][nc] == 'K':
                    print("Success")
                    return
                if rows[nr][nc] != '.':
                    break
                nr += dr
                nc += dc

    #queen
    for r, c in queen.addr:
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            while inboard(nr, nc):
                if rows[nr][nc] == 'K':
                    print("Success")
                    return
                if rows[nr][nc] != '.':
                    break
                nr += dr
                nc += dc

    #pawn
    for r, c in pawn.addr:
        directions = [(-1,-1), (-1,1)]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if inboard(nr, nc):
                if rows[nr][nc] == 'K':
                    print("Success")
                    return

    print("Fail") # หลุดมาถึงตรงนี้ คือรอด
    # while ใช้กับหมากพุ่งไกล
    # if ใช้กินช่องเดียว