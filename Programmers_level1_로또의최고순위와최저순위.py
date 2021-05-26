def solution(lottos, win_nums):
    unknown  = 0
    correct = 0
    for i in lottos:
        if i == 0:
            unknown += 1
            continue
        if i in win_nums:
            correct += 1
    max_rank = -1 * (correct + unknown) + 7
    min_rank = -1*correct + 7
    if max_rank == 7:
        max_rank = 6
    if min_rank == 7:
        min_rank = 6
    return [max_rank, min_rank]