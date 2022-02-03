# import random 정리
# 단어의 길이 정리   #word_len=int(len(answer)) 

# 알게 된점// 각각의 if문으로 여러가지의 상황을 만들어 낼수 있다. , 번갈아가면서 출력 for문

import random                                  
word=['python','programing','line','hangman']
answer=random.choice(word)     # random 모듈을 통해 word 중에서 임으로 단어 선택
letters=''

left=6   # 시도 횟수 

while True:   
    underbar=True
    for i in answer:         # 정답인 단어와 선택한 알파벳 비교하며 " 알파벳 or _ "출력함
        if i in letters:
            print (i,end=' ')  
            
        else:
            underbar=False
            print ('_',end=' ')
    print()

    if underbar :
        print('SUCCESS')
        print('word = ',answer)    
        break

    letter=input('Input letter > ')
    letters=letter+letters           # 기존의 단어와 새로입력된 단어의 합

    if letter in answer:
        print('Correct')
        
    
    else:
        print('Wrong',end=' ')
        left=left-1
        print('남은 시도 횟수:',left) 
        if left==0:
            print('word = ',answer)
            break
    print()