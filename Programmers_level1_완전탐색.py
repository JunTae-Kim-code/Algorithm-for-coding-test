def solution(answers):
    answer = []
    a1 = [ 1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    for i in range(len(answers)):
        if a1[i%5] == answers[i]:
            c1+=1
        if a2[i%8] == answers[i]:
            c2+=1
        if a3[i%10] == answers[i]:
            c3+=1
    total = [c1,c2,c3]
    print(total)
    max_c = max(total)
    if max_c == c1:
        answer.append(1)
    if max_c == c2:
        answer.append(2)
    if max_c == c3:
        answer.append(3)
    return answer