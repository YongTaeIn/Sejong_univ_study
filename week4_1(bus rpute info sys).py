## pip install xlrd //pip install pandas
# 파이썬 엑셀 데이터 추출 정리

# 정류장 이름 함수 선언
def station_name():
    for i in range(Row): 
        if name_1 in data_np[i][6]:
          print('[{}] 정류소에서 [{}] 버스가 정차합니다.'.format(data_np[i][6],data_np[i][1]))

# 버스 노선명 함수 선언
def line_num():
    for i in range(Row):
        if name_2 in data_np[i][1]:
            print('[{}] 버스가 [{}] 정류장에서 정차합니다.'.format(name_2,data_np[i][6]))


#패키지 선언
import pandas as pd
#파일 경로 설정
Location ='D:\Git\Git\GitHub\YONGTAEIN_TSET\파이썬'
File  = 'bus_info.xls'                                #엑셀 확장자로 오픈
#추출행 ,열 선언
Row=39363
Column=8
#추출 및 변환 코드
data_pd=pd.read_excel('{}/{}'.format(Location,File),         #전체 값
            header=None,index_col=None,names=None)
data_np=pd.DataFrame.to_numpy(data_pd)                      # 행,열 의 요소 값


while True:
    print('''\
==================================
1. 정류장 정차 버스 찾기
2. 버스노선의  정차 정류장 찾기
3. 종료
==================================
    \
    ''')
    input_1=int(input('정수값을 입력하시오: '))

    if input_1==1:
        name_1=input('정류장 이름을 입력하세요(일부 명칭도 가능):')
        station_name()

    if input_1==2:
        name_2=input('버스노선명을 입력하시오 : ')
        line_num()
        
    if input_1==3:
        break