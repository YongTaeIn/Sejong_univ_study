from collections import deque    # ' collections ' =라이브러리, 'deque' = 메서드

   
def bfs(graph, start, visited): # 너비 우선 탐색
    queue = deque([start])      # 시작 노드를 큐에다가 먼저 삽입(삽입할 때 파이썬 리스트[]로 감싸주기)
    visited[start] = True       # 시작 노드를 방문 처리

                            # 큐에서 노드를 pop하고 그 노드의 인접노드들을 탐색. 단, 큐가 빌(False)때 까지//  []가 false임
    while queue:            # 빈 리스트가 될때까지 반복함
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:        # for 문을 통해 인접한노드(가까운노드)부터 탐색
            if not visited[i]:
                visited[i] = True
                queue.append(i)
 
def dfs(graph,v,visited):              # 깊이우선탐색 _ 재귀 함수 이용, 스택을 이용
    visited[v]=True
    print(v,end=' ')

    for i in graph[v]:                 # grpah에 있는 노드 찾음
        if not visited[i]:             # visited[i] 가 False 일경우에 실행
            dfs(graph,i,visited)       # graph 와 visited 는 그대로 계속 가야함 
                                       # (그래야 이전 정보가 게속 연결되니깐)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited=[False]*9      # 방문하지 않은 노드 False로 표현,방문한 노드를 True로 표현 

# 정의된 함수 호출
dfs(graph,1,visited)   # 0번 노드가 없으니 1번노드부터 탐색
bfs(graph,1,visited)