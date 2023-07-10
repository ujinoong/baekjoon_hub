import sys
def buy_triple(idx): # 7원 구매할 때 함수
    global cost
    k = min(x[idx: idx + 3]) # k는 구매횟수
    x[idx] -= k
    x[idx + 1] -= k
    x[idx + 2] -= k
    cost += 7 * k

def buy_double(idx): # 5원 구매할 때 함수
    global cost 
    k = min(x[idx: idx + 2])
    x[idx] -= k # 구매횟수만큼 차감되는 물건 갯수
    x[idx + 1] -= k
    cost += 5 * k

def buy_one(idx): # 3원 구매할 때 함수
    global cost
    cost += 3 * x[idx]

N = int(sys.stdin.readline()) # 공장 개수
x = list(map(int, sys.stdin.readline().split())) + [0, 0] 
cost = 0
for i in range(N):
    if x[i + 1] > x[i + 2]:
        k = min(x[i], x[i+1] - x[i+2])
        x[i] -= k
        x[i+1] -= k
        cost += 5 * k

        buy_triple(i)
    else:
        buy_triple(i)
        buy_double(i)
    buy_one(i)
    
print(cost)