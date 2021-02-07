#<input>
# N : 방 번호

#<output>
# 몇개의 방을 지나가야 하는지 출력한다.

destination = int(input()) - 1
i = 0
tail = 0


while(1):
    tail += 6 * i
    
    if destination <= tail:
        print(i+1)
        break;
    i+=1
    
    
    
    
    
    
    
#[0]  6 * 0
#[1, 2, 3, 4, 5, 6]  => 6 * 1
#[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] => 6 * 3
#[19, ...., 36] 6 * 6 
#[37, .....] 6 * 10
# [61, ....]
    