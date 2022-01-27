#하노이 탑 과제--기둥의 위치는 안바뀌고 기둥의 역할이 바뀜

N=int(input())          # N개의 개수 입력받음

def hanoi(N, A, B, C):      # N은 개수 A,B,C 는 막대기      A=시작, B= 목표, C=보조
    
    if N ==1:             # 원판 1개를 A에서C로 옮긴다.        
        print(A,C)      # A시작점 ,C종착점
    else:
        hanoi (N-1,A,C,B)      #원판 n-1개를 A에서 B로 옮김   (n-1개를 보조로 옮김)
        print(A,C)  
        hanoi (N-1,B,A,C)      #원판 n-1개를 B에서 C로 옮김    (목적지로 이동시킴)

print(2**N-1)                # 원판의 개수에 따른 일반화 한 식 

if N<=20 :                   # 20개 이하일때만 출력이 되어야함
    hanoi(N,1,2,3)    
