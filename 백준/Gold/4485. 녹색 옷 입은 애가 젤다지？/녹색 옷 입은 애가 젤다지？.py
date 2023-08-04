import heapq, sys

def dijkstra(graph, cost, x, y):
    n = len(graph)
    pq = []
    # 시작노드로 가기 위한 최단 경로 큐에 삽입
    heapq.heappush(pq, (graph[x][y], x, y))
    while pq:
        curr_cost, curr_x, curr_y = heapq.heappop(pq)
        if cost[curr_x][curr_y] < curr_cost:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                next_cost = graph[next_x][next_y]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if curr_cost + next_cost < cost[next_x][next_y]:
                    heapq.heappush(pq, (curr_cost + next_cost, next_x, next_y))
                    cost[next_x][next_y] = curr_cost + next_cost
    return cost[n-1][n-1]

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
INF = int(1e5)
tc = 1

while True:
    n = int(input())
    if n == 0: break
    # 그래프 n만큼 입력받고 노드 정보 담는 리스트 만들기
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 최단 거리 테이블 모두 무한으로 초기화
    cost = [[INF] * n for _ in range(n)]

    # 결과
    answer = dijkstra(graph, cost, 0, 0)
    print('Problem {}: {}'.format(tc, answer))
    tc += 1