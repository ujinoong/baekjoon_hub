# 백준 8958 OX퀴즈

n = int(input())

for _ in range(n):
    answer_list = list(input())
    score = 0
    sum_score = 0
    for i in answer_list:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)