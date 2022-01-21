import math

#기본 클래스 선언중

class calculator:  #  붕어빵 틀 
    
    def __init__(self,first,second):           # 생성자를 통해 반드시 필요한 부분을 선언함.// ★매개변수 self에는 객체★, first=n, second=k 가 할당됨
        self.first=first                       # 첫번째(n=first)로 받은 요소를 self.first 할당함
        self.second=second                     # 두번째(k=second)로 받은 요소를 self.second 할당함
    
    def add(self):                             # 호출한 알맞은 메서드를 찾아가서 수행함.
        return self.first + self.second  
    
    def subtraction(self):        
        return self.first - self.second

    def mul(self):        
        return self.first * self.second
    
    def div(self):
        return self.first / self.second

# 상속된 클래스 선언중 -내부 모듈 이용
class improved_calculator(calculator):          #  붕어빵 틀    
    def square(self):   # 제곱
        return math.pow(self.first, self.second)
    
    def common(self):  # 최대 공약수
        return math.gcd(self.first, self.second)

while 1:
    print('''\
아래에 사용을 원하시는 사칙연산을 선택해주세요!
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 제곱
6. 최대 공약수
7. 종료\
        ''')
    num =int(input())               # num으로 받아들인 숫자에 의해서 if구문을 이용해 조건문을 만듬
    if num==7:
        print("계산기 프로그램을 종료합니다")
        break
    
    n,k =map(int, input("두 숫자를 입력해주세요: ").split())        # map함수를 이용해 한번에 두개의 입력을 int형으로 받음
    
    a=improved_calculator(n,k)      # ★(붕어빵) a객체가 사용할 입력 2개(n.k)를 알려줌 //a 객체는 improved_calculator의 인스턴스
    
    if num==1:                      
        print(a.add())        # add라는 메서드가 수행되면 self에는 a가 입력 ->생성자를 통해 n,k의 값을 first,second로 할당후 add메서드를 실행함->출력
        print()
    if num==2:
        print(a.subtraction())
        print()
    if num==3:
        print(a.mul())
        print()
    try:                             # try except 구문을 사용하여  에외가 발생할수 있는 코드를 넣어주고 
        if num==4:
            print(a.div())
            print()
    except:                          # except구문으로 예외가 발생시 실행할 코드를 작성해 줌
        print("0으로 나눌 수 없습니다.")
        print("None")
        print()
        
    if num==5:
        print(a.square())
        print()
    if num==6:
        print(a.common())
        print()
    