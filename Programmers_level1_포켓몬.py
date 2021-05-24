def solution(nums):
    answer = 0
    kind=set()
    for i in nums:
        kind.add(i)
    if len(kind)>=len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(kind)
    return answer