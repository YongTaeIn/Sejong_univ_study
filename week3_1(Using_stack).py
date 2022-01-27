import sys

class Stack_1:
    def __init__(self):         #c=self가 됨
        self.a=[]      # 빈리스트에 선언
    
    def push(self, num):                           # Push 메소드 선언
        self.a.append(num)                         # 정수 추가        
            
    def pop(self):                                    # if else 사용 
        if self.a == []:   
            print(-1)                            
            return                                
        else:                                        
            b=self.a[-1]                       # 맨 마지막 스택 출력
            self.a.pop(-1)                             # 스택에 가장 위에있는 정수 제거
            print(b) 
            return                    
        
    def size(self):
        return print(len(self.a))                     # 정수의 개수 출력
    
    def empty(self):                                 # if else 로
        if self.a ==[]:                               # 스택이 비면 1출력
            return print(1)
        else:
            return print(0)
    
    def top(self):
        if self.a==[]:                                # 스택이 비면 -1 출력
            print(-1)
            return 
        else:                                    # 가장 위에있는 정수 출력            
            print(self.a[-1])
            return 
            
c=Stack_1()                                      # c라는 객체 선언          ★ ()안침

print('명령의 수 : ',end='')
N=int(input())

for i in range(N):      # N개의 명령어 실행
    k=sys.stdin.readline().split()   
    d=k[0]
        
    if d == "push":
        c.push(k[1])
    elif d == "pop":    
        c.pop()
    elif d == "size":
        c.size()
    elif d == "empty":    
        c.empty()
    elif d == "top":
        c.top()                        # ★ ()안침