# 전화번호부

def solution(phone_book):
    
    # 해시 선언
    hash = {}
    
    # 해시 초기화
    for i in phone_book:
        hash[i] = 1
        
    # 해시 돌면서 확인
    for i in phone_book:
        # 접두어를 확인하기 위한 string 변수 생성
        target = ""
        for j in i:
            target += j
            if target in hash and target != i:
                return False
    return True    
    
    