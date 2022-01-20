import math
import os
import random
import re
import sys

def miniMaxSum(arr):          # 5개를 입력을 받음
    arr_2 =arr[:]         # arr_2 , arr 복사함  
    #최솟값 4개 찾고 더하기
       #->가장 큰값을 빼주고 나머지를 sum함수로 더해서 출력  (최댓값 인덱스 찾고, 그 인덱스를 제거)
    max_1=max(arr)  # 리스트에서 최댓값을 찾고
    max_2=arr.index(max_1)    #리스트에서 최대값의 인덱스를 찾음, 인덱스는 0부터 시작
    del arr[max_2]               # 리스트에서 최댓값을 제거한 리스트
    max_add=sum(arr)             # 
    
    ####최댓값 4개 찾고 더하기(최솟값 제거)
    min_1=min(arr_2)  # 리스트에서 최솟값을 찾고
    min_2=arr_2.index(min_1)  #리스트에서 최솟값 인덱스를 찾음, 인덱스는 0부터 시작
    del arr_2[min_2]  #print("최솟값 제거한 리스트",arr)
    min_add=sum(arr_2)
    print(max_add,min_add)
    
if __name__=='__main__':
    arr=list(map(int,input().rstrip().split()))    
    miniMaxSum(arr)