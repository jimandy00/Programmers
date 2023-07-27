from collections import defaultdict

# info == 어느 노드에 양과 늑대가 있는지 알려주는 지도
# edges == 트리 정보가 담겨있는 리스트
def solution (info, edges):
    # global 변수로 선언하여 다른 함수에서도 해당 변수를 사용 가능하게 만듦
    global graph, animalInfo, answer

    #dfs 함수에서 info(==animalInfo)를 사용해주기 위한 작업
    animalInfo = info

    answer = 0

    # 노드간의 정보를 인접 노드끼리 연결하여 재구성
    # 글로 풀어진 트리를 그림을 그려 트리구조로 만드는 과정이라고 생각함
    graph = defaultdict(list)
    for p, c in edges:
        graph[p].append(c)

    # 초기 dfs 함수 실행
    dfs(0, 0, 0, [])
    return answer

# DFS함수
# current : 현재 위치한 노드
# possible : 현재 위치한 노드에서 갈 수 있는 노드들(인접한 노드)
def dfs(current, sheep, wolf, possible):
    global graph, animalInfo, answer
    
    # 현재 위치한 노드에 해당하는 동물이 있는지 info에서 찾기
    # info는 지도라고 생각하고 풂
    if animalInfo[current] == 0:
        sheep += 1
        answer = max(answer, sheep) # answer는 global변수이므로 dsf 함수 내에서 바로 사용 가능
    else:
        wolf += 1

    if sheep <= wolf:
        return 

    #recursive
    # 현재 노드에서 인접한 노드들은 추가
    possible.extend(graph[current])
    for j in possible:
        # 인접한 노드들을 계속 타고타고타고 들어가는 과정
        # possible자리에는 possible에서 들리지 않는 노드만 가겠다(?)는 의미의 로직 작성
        dfs(j, sheep, wolf, [i for i in possible if i != j])

    
    