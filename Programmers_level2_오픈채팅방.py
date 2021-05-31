def solution(record):
    user = {}
    for message in record:
        if message[0] == 'L':
            continue
        action, user_ID, ch = message.split(' ')
        user[user_ID] = ch
    print_list = []
    for message in record:
        if message[0] == 'L':
            action, user_ID = message.split(' ')
        else:
            action, user_ID, ch = message.split(' ')
        if action == 'Enter':
            print_list.append(user[user_ID]+'님이 들어왔습니다.')
        elif action == 'Leave':
            print_list.append(user[user_ID]+'님이 나갔습니다.')    
    return print_list