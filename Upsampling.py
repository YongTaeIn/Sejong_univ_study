# 업샘플링 과제

import sys    # 프로그램 시간초과를 방지하기 위해서.

n, k = map(int, sys.stdin.readline().split())  # n,k로  받음 

list1 = []                         # 빈 리스트를 설정

for i in range(n):                # n의 사이즈에 따라서 반복 함 
    list1.append(list(map(int, sys.stdin.readline().split()))) # 2차원 리스트 입력받기 [[1,0],[0,1]]
# print(list1)

for i in range(n):             
    for _ in range(k):
        for j in range(n):
            for _ in range(k):            #동일한값을 출력을 시키기위해서 for루프 돌림, _역할 =k번 반복
                print(list1[i][j], end = ' ')    # end=' ' 줄바꿈 안하고 이어서 출력함
        print()          # 행을 바꿔주는 역할을 함