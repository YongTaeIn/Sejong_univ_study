def boat(people,limit):   
    
   anwser =0
   S=0  #start
   E=N-1                      #리스트의 순서는 뒤에서 부터임으로
   while S<=E:                              # 배열의 순서 따라감
      if people[S]+people[E] <= limit:     # 맨앞과 맨뒤의 값을 합 함으로  2명에서 타고나감
         E=E-1
         S=S+1                            
      else:                                # 가장 무거운 사람은 혼자 타고감.
         E=E-1                            # 그 다음으로 무거운 사람 찾아줌
      
      anwser=anwser+1        # while문 내부에 증가하도록 if조건문을 만들어줌
   return print(anwser)

N=int(input("인원을 입력하세요.\n"))                              
limit=int(input("구명보트의 무게 제한을 입력하세요.(40~240)\n"))       
print(N,"명의 몸무게를 입력하세요")


people=[]
for _ in range(N):           
    A=int(input())
    people.append(A)       
    
people.sort()             

boat(people,limit)