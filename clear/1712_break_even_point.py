# <input>
# A : 고정비용 (임대료 + 재산세 + 보험료) 등 
# B : 가변비용 (재료비 + 인건비)
# C : 노트북 판매가
# => 셋모두 21억 이하의 자연수

# <output>
# 최초로이익이 발생하는 판매량을 출력한다.

# prior knowledge
# 손익분기점( break_even_point ) : 총 수입이 총 비용보다 많아져서 이익이 발생하는 지점



def break_even_point(f_m, d_m, price):
    profit = price - d_m
    sales = 0
    
    if profit <= 0:
        return -1
    else:
        return f_m // profit + 1
        
        
f_m, d_m, price = map(int, input().split())
print(break_even_point(f_m, d_m, price))

#해설 : 
#1. 판매가에서 재료비를 빼야 순수익(profit)이 나온다.
#2. 가변비용이 판매가보다 크거나 같거나해서 이익이 생기지 않는 경우는 바로 -1을 return한다.
#2. 고정비용을 순수익으로 나눠서 몫에다 +1 을 해주면 몇번의 판매 수량이 손익분기점을 넘기는지 구할수 있다.

        
#break point
#1. 백준에서 input을 줄때는 한 줄로 주기때문에 input() input() 이렇게 받을 수 없고, input을 string으로 받아서 split하여 int로 변환해주어야 한다.
