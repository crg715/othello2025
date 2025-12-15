from .sort import SortGame

# ===========================
# myai: 貪欲に最大枚数を取るオセロAI
# ===========================

def myai(board, color):
    """
    board: 2D list of ints  
        0 = 空き, 1 = 黒, 2 = 白
    color: int  
        1 = 黒番, 2 = 白番
    戻り値: (col, row) 置く場所
    """

    # 方向ベクトル (8方向)
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),         (1,  0),
                  (-1,  1), (0,  1), (1,  1)]

    opponent = 1 if color == 2 else 2
    height = len(board)
    width  = len(board[0])

    def valid_move_and_flips(r, c):
        """
        (r,c) が合法手か判定し，
        ひっくり返せる石座標リストを返す（合法手でない → 空リスト）
        """
        if board[r][c] != 0:
            return []

        total_flips = []
        for dy, dx in directions:
            flips = []
            y, x = r + dy, c + dx
            # 敵を挟む方向を探す
            while 0 <= y < height and 0 <= x < width and board[y][x] == opponent:
                flips.append((y, x))
                y += dy
                x += dx

            # 間に味方があれば有効
            if flips and 0 <= y < height and 0 <= x < width and board[y][x] == color:
                total_flips += flips

        return total_flips

    best_move = None
    best_gain = -1

    # 全セル走査
    for r in range(height):
        for c in range(width):
            flips = valid_move_and_flips(r, c)
            if flips:
                # 取れる枚数が最高の手を選ぶ
                if len(flips) > best_gain:
                    best_gain = len(flips)
                    best_move = (c, r)  # (col, row)

    # 合法手があれば返す，なければパス扱い (None)
    if best_move is not None:
        return best_move
    else:
        # パス (合法手なし) の場合，
        # None を返す / または適宜 (−1, −1) などに変更
        return None
