import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dq = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1: # 상어가 있는 위치
            dq.append([i, j])

result = 0
# 상어끼리의 최단 거리
while dq:
    x, y = dq.popleft()
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if board[nx][ny] != 0:
            continue
        dq.append([nx, ny])
        board[nx][ny] = board[x][y] + 1
        result = max(result, board[x][y] + 1)

print(result - 1)