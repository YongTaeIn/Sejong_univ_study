#구구단 출력문제

while True:                                           #무한 루프를 통해 1,2를 선택시 또다시 출력이 되게 함.
    print("""\
--------------------------------------------------
\"구구단을 외자,구구단을 외자\" 프로그램을 실행합니다.
1.홀수 구구단
2.짝수 구구단
3.종료
----------------------------------------------------
\
""")

    i=int(input("숫자를 입력하세요: "))                 # 숫자를 입력하는 부분  ,입력된 숫자 i=1,2,3 임
                                                       #int 형식으로 바꾸어 주었기 때문에while 문에서 i=="숫자" 큰따옴표 안함.

    while i==1:                                        # if를 쓰지 못하는 이유  : if를 사용하게 되면 a==9 부분의 break 가 while True 를 깨버려서 프로그램이 종료됨                                 
        for a in range(3,10,2):                        # 3단,5단,7단,9,단 출력  (이중 for loop)    
            print("{}단".format(a))   
            for b in range(1,10):                       #뒤에 있는 숫자 돌려줌
                print("{}*{}={}".format(a,b,a*b))
        if a==9:
            break        
    
    while i==2:
        for a in range(2,10,2):                                # 2단,4단,6단,8단 출력  (이중 for loop)
            print("{}단".format(a))   
            for b in range(1,10):                             #  뒤에 있는 숫자 돌려줌
                print("{}*{}={}".format(a,b,a*b))
        if a==8:
            break
            

    while 3<i or i<0 :                                         
        print("잘못 입력 하셨습니다. 1~3 번 숫자를 입력하세요.")
        break
    
    if i==3:                                       # while i==3 으로 하면 반복문임으로 break 를 하나 더 추가해서 종료시켜야하는데 그렇게 하면 
        print("프로그램을 종료합니다.")              # 다른 while 문의 break 와 break 가 이중으로 걸려서 프로그램이 while True 가 무용지물이 된다.
        break
                    
        