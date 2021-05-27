def solution(board, moves):
    count = 0
    basket = []
    for i in moves:
        pick = i-1
        for pos in range(len(board)):
            if board[pos][pick]:
                basket.append(board[pos][pick])
                board[pos][pick] = 0
                break
        if len(basket) >1 and basket[-1] == basket[-2]:
            count += 2
            del basket[-1]
            del basket[-1]
    return count