def solution(numbers, hand):
    answer = ''
    cur_left = '*'
    cur_right = '#'
    left_dist = []
    right_dist = []
    left = {1:0, 4:1, 7:2, '*': 3, 2:4, 5:5, 8:6, 0:7}
    right = {3: 0, 6:1, 9:2, '#':3, 2:4, 5:5, 8:6, 0:7}
    mid = {2:0, 5:1, 8:2, 0:3}
    for i in range(4): # 147*->2580, 369#->2580
        sub = []
        for j in range(4):
            sub.append(abs(i-j)+1)
        left_dist.append(sub)
        right_dist.append(sub)
    for i in range(4): # 2580->2580
        sub = []
        for j in range(4):
            sub.append(abs(i-j))
        left_dist.append(sub)
        right_dist.append(sub)
    
    for i in numbers:
        if i==1 or i==4 or i==7:
            cur_left = i
            answer+='L'
        elif i==3 or i==6 or i==9:
            cur_right = i
            answer+='R'
        else:
            if left_dist[left[cur_left]][mid[i]] < right_dist[right[cur_right]][mid[i]]:
                cur_left = i
                answer+='L'
            elif left_dist[left[cur_left]][mid[i]] > right_dist[right[cur_right]][mid[i]]:
                cur_right = i
                answer+='R'
            else:
                if hand=='right':
                    cur_right = i
                    answer+='R'
                else:
                    cur_left = i
                    answer+='L'               
    return answer