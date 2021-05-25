def solution(new_id):
    id = list(new_id.lower()) # 1
    # 2
    num_id = len(id)
    for i in range(num_id):
        if id[num_id-i-1].islower() or id[num_id-i-1].isdigit() or id[num_id-i-1]=='-' or id[num_id-i-1]=='_' or id[num_id-i-1]=='.':
            continue
        del id[num_id-i-1]
    # 3
    num_id = len(id)
    for i in range(num_id-1):
        if id[num_id-i-1]=='.' and id[num_id-i-2]=='.':
            del id[num_id-i-1]
    # 4
    if len(id)>0 and id[0] == '.':
        del id[0]
    if len(id)>0 and id[-1] == '.':
        del id[-1]
    #5
    if id == []:
        id.append('a')
    #6
    if len(id)>15:
        id = id[:15]
    if id[-1] == '.':
        del id[-1]
    #7
    if len(id) < 3:
        last = id[-1]
        while True:
            if len(id)==3:
                break
            id.append(last)         
    return ''.join(id)