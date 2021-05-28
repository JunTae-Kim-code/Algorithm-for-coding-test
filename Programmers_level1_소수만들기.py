def solution(nums):
    # 1+2+3 = 6 min
    # 998+999+1000 = 2997 max < 53*59
    # 소수: 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59
    #짝+짝+짝 = 짝, 짝+홀+홀=짝, 짝+짝+홀 = 홀, 홀+홀+홀 = 홀
    sosus = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum_num = nums[i]+nums[j]+nums[k]
                if sum_num in sosus:
                    count+=1
                elif sum_num > 59:
                    flag = 1
                    for sosu in sosus:
                        if sum_num%sosu == 0:
                            flag = 0
                            break
                    if flag:
                        count+=1                                    
    return count