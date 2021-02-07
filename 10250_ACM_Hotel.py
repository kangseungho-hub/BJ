#<description>
# 정문에서부터 엘리베이터까지의 거리는 무시, 즉 엘리베이터까지의 거리가 정문까지의 거리인것이다.
# 두 방 사이의 거리 1
# 방번호는 YXX, YXXX형태 Y : 층수 X : 엘리베이터부터 셌을 때 번호
# 손님은 엘리베이터를 타고 내려가는 시간은 고려하지 않지만 엘리베이터까지 거리가 같을때는 아래층을 선호


#<input>
# T : T개의 테스트 데이터가 입력됨을 나타낸다. ex) 2 \n 6 12 10 \n 30 50 72 
# H : 호텔의 높이
# W : 방의 개수
# N : 몇번째 손님인지
# 1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W

#<output>
# 각 테스트데이터마다 정확히 한 행으로 N번쨰 손님에게 배정되어야 하는 방을 출력해야한다.




#<solving>
# 1. 테스트데이터의 개수를 확인하고, 해당 개수만큼 테스트데이터를 받는다.
testData_count = int(input())
testCases = []
def to_two_digits(number):
    return ("0" + str(number) if number // 10 == 0 else str(number))
    
    
def solving(H, W, N):
    floor = 0
    room = 1
    
    for i in range(N):
        if floor == H:
            room += 1
            floor = 1
        else:
            floor += 1
    
    print(str(floor) + to_two_digits(room))
  
for i in range(testData_count):
    testCases.append(list(map(int, input().split())))

for testCase in testCases:
    solving(testCase[0], testCase[1], testCase[2])
    




    


    
            
        
        
        
        



