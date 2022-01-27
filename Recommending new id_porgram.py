# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다. 
new_id=input(" 아이디를 입력해주세요.").lower()                             # .lower함수를 사용하여 대문자를 소문자로 치환함.
 
 
# 2단계  new_id 에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다. 
delete = "~!@#$%^&*()=+[{]}:?,<>/"                        
for i in range(len(delete)):                              # len() 함수: 문자열길이구함    ->    range() 함수 : 정수의 범위를 나타내는 값
    new_id =new_id.replace(delete[i],"")                  #remove 함수를 이용하여  delete내부에 있는 문자열을 하나씩 다 공백으로 바꿈// 
                                                      # remove(문자열에서 바꾸고 싶은 문자,새로 바꿀 문자,변경 횟수)  : 횟수를 입력 안했음으로 다 제거함.

# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
double=".."
for i in range(len(double)):                          
    new_id =new_id.replace(double,".")                  #동일한 방식으로 ".." 자체를 하나의 문자로 보고 double을 넣음.


# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. 
if new_id !='':    
    if new_id[0] ==".":
        new_id = new_id[1:]       
    elif new_id[-1]==".":                                       
       new_id = new_id[:-1]       
        
        
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
if new_id == '' :                               #new_id가 빈문자열이면
    new_id=new_id.replace('','a')               #빈칸을 a로 치환합니다.
    
    
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침
# 표(.) 문자를 제거합니다. 
if len(new_id)>15:
    new_id=new_id[:15]                     #슬라이싱을 이용해서 0~15까지만 살림.
    if new_id[-1]==".":
        new_id = new_id[:-1]
        
else:                                       # 길이가 16미만인데 마침표가 끝에 위치할수도 있기때문에 제거해줌
    if new_id[-1]==".":
        new_id=new_id.replace(new_id[-1],"") 
      

#7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때 까지 반복해서 끝에 붙입니다.
while len(new_id)<=2:
    new_id=new_id+new_id[-1]    
print(new_id)

