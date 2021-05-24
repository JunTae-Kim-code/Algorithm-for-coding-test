def solution(n, lost, reserve):
    check = []
    for i in reserve:
        for j in lost:
            if i == j:
                check.append(i)
    for i in check:
        lost.remove(i)
        reserve.remove(i)
    count = 0
    reserve.sort()
    lost.sort()
    recieve = []
    for i in reserve:
        for j in lost:
            if j not in recieve and i-1 == j:
                count+=1
                recieve.append(j)
                break
            if j not in recieve and i+1 == j:
                count+=1
                recieve.append(j)
                break
    return n - (len(lost) - count)