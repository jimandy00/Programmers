# 2023년 9월 7일 목요일

def solution(nums):
    hash = {}

    for i in nums:
        hash[i] = 1

    # 가져갈 수 있는 포켓몬 수
    bring = len(nums) // 2

    if(len(hash) < bring):
        answer = len(hash)
    else:
        answer = bring

    return answer