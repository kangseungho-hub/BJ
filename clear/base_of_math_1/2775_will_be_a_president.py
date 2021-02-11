def solution(k, n):
    temp_floor = list(range(1, n + 1))
    
    for j in range(k):
        for i in range(n):
            if i == 0:
                pass
            else:
                temp_floor[i] = temp_floor[i] + temp_floor[i-1]
            
    print(temp_floor[n-1])


test_case_count = int(input())
k_n_list = []



for _ in range(test_case_count):
    k_n_list.append([int(input()), int(input())])
    
for k, n in k_n_list:
    solution(k, n)