import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix = 0
    if scoville[0]>=K:
        return 0
    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
        mix += 1
        if scoville[0]>=K:
            return mix
        if len(scoville)<2:
            if scoville[0]>=K:
                return mix
            return -1
