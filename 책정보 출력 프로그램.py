#책 정보 출력 프로그램

book_info={ 
    "HarryPotter1" : [[1997],[6],[26]],               #book_info 딕셔너리를 선언해줌
    "TheLordOfTheRings" : [[1954],[7],[29]],
    "engineering_mathematics1" :[[2018],[2],[28]]
}
    
while True:                                           # 무한반복문을 입력해서
    title=input("원하시는 책을 입력하세요 \n")


    if title in book_info:                             # title 이 book_info 라는 딕셔너리의 key값에 존재한다면
        num=int(input("""\
    ------------------------------
    원하시는 정보를 선택해 주세요
    1. 년
    2. 월
    3. 일
    4. 종료
    -------------------------------    
\
"""))
        if num==1:                                            # 1을 선택했을경우 
            print( book_info[title][0],"년 입니다.")           # 딕셔너리를 활용해서 편하게 key값을 찾아 들어가고 거기에 맞는 인덱스 번호(0번)을 리스트에서 찾아간다. 
        elif num==2:                                          #값 자체가 리스트 이기 때문에 값에 알맞음 인덱스번호(0번)을 찾아감
            print(book_info[title][1],"월 입니다.")
        elif num==3:
            print(book_info[title][2],"일 입니다.")
        else:
            print("프로그램이 종료되었습니다.")
            break                                             # break를 활용하여 무한 while loop을 탈출한다.
            
            
    else:
        print("제목을 다시 입력해주세요")                                
