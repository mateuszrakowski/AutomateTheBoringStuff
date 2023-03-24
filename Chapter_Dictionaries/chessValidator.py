import re, sys
    

board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

piecesVariations = ["bking", "bqueen", "brook", "bknight", "bbishop", "bpawn",
"wking", "wqueen", "wrook", "wknight", "wbishop", "wpawn"]


def main():
    print(isValidChessBoard(board))


def isValidChessBoard(board):
    totalPieces = {}

    # Check if position is valid
    for k, v in board.items():
        pos = re.search(r"[1-8][a-h]", k)
        if not pos:
            sys.exit("Wrong position on board.")
        
        # Check if type of piece is valid
        prefix = re.search(r"^w|^b|^$", v)
        if not prefix:
            sys.exit("Wrong piece type.")

    # Count pieces on the board
    boardPieces = list(board.values())
    for p in piecesVariations:
        totalPieces[p] = sum(1 for i in boardPieces if p in i)

    # Check if number of pieces is valid
    if totalPieces["bking"] != 1 or totalPieces["wking"] != 1:
        sys.exit("Wrong number of Kings.")
    if totalPieces["bqueen"] > 1 or totalPieces["wqueen"] > 1:
        sys.exit("Wrong number of Queens.")
    if totalPieces["brook"] > 2 or totalPieces["wrook"] > 2:
        sys.exit("Wrong number of Rooks.")
    if totalPieces["bknight"] > 2 or totalPieces["wknight"] > 2:
        sys.exit("Wrong number of Knights.")
    if totalPieces["bbishop"] > 2 or totalPieces["wbishop"] > 2:
        sys.exit("Wrong number of Bishops.")
    if totalPieces["bpawn"] > 8 or totalPieces["wpawn"] > 8:
        sys.exit("Wrong number of Pawns.")
    
    return "Chess board is valid!"


if __name__ == "__main__":
    main()