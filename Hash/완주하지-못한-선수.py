# 2023년 08월 29일 화요일
# 프로그래머스 - 해시 - level 1 - 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# Participant = ["참여한 사람 명단"]
# Completion = ["완주한 사람 명단"]
# return = 완주 못한 사람

# Hash에 참여한 사람 명단을 넣고
# value를 1로 만든다.
# 동명이인이라면? value를 +1 한다.

# 완주한 사람 명단을 참여한 사람 명단에서 찾는다.(key)
# 값이 1이라면 Hash에서 삭제하고
# 1보다 크다면 동명이인이니 -1을한다.

# 최종적으로 hash에 남은 사람을 출력한다. == 미완주자

def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    
    for i in completion:
        if hash[i] == 1:
            del hash[i]
        else:
            hash[i] -= 1
    
    
    answer = list(hash.keys())[0]
    return answer


        