# 리스트로 구현한 노드 
def dfs(graph ,start_node):
    need_visit=list()    # 방문해야하는 노드   // 항상 두개의 리스트를 별도로 관리해주는것이 포인트
    visited=list()       # 방문한 노드
    
    need_visit.append(start_node)   #시작노드 설정
    
    while need_visit:               # 방문이 필요한 노드가 있다면 
        node=need_visit.pop()       # 그중에서 마지막 데이터 추출(스택 구조)
        if node not in visited:     # 방문한 목록 노드에 없다면
            visited.append(node)    # 방문한 목록 노드에 추가하고 
            need_visit.extend(graph[node])  # 방문해야 하는 노드에 연결된 노드 추가
    return visited



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
print(dfs(graph, 1))
