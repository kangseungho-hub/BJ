#<input>
# N : weight(kg) of sugar

#<output>
# count of mininal sugar bag
# if can't make N kg with 3, 5kg sugar bag, just print -1

N = int(input())


def solution(N):
    answer = 0
    
    if N // 5 != 0:
        a = N // 5
        answer += a
        rest = N % 5

        if rest % 3 == 0:
            answer += rest // 3
        elif rest == 1:
            answer += (2-1)
        elif rest == 4:
            answer += (3-1)
        elif rest == 2 and a > 1:
            answer += (4-2)
        else:
            answer = -1
        return answer
    
    elif N == 3:
        return 1
    else:
        return -1
    
print(solution(N))





        

#해설, 일단 다짜고짜 5로 나눈다. 그러면 0, 1, 2, 3, 4만 나올수 있을거잖아? 6, 7, 8, 9는 나머지로 절대 나올 수 
#없고, 그러면 여기서 1, 2, 3, 4를 만들 수 있는 방법은 딱 정해져있다. 
#1인경우 : 5봉투를 하나 빼서 3키로를 2개 채우게되면 나머지 1kg인 경우를 처리 가능
#4인경우 : 5봉투를 하나빼고서 3키로 3개 채우게되면 나머지 3kg인 경우를 처리 가능
#2인경우 : 5봉투를 두개 빼고서 3키로를 4개 채우게되면 나머지 2kg인 경우를 처리 가능
#!!!@@@가장 중요한거는 나머지가 0,1 ,2, 3, 4 일 수 밖에 없는 것을 이해하는 것이었다.

        
    
    
    

    
        
    

    
        
        

