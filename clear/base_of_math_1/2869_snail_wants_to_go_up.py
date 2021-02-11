import math
#<input>
# V : the height of the tree that snail will climb
# A : the height of snail can climb at the day
# B : the height of snail be sliped at the night
#(1 ≤ B < A ≤ V ≤ 1,000,000,000)


#<output>
# the day it takes for the snail reach at the top of the tree

A, B, V = map(int, input().split())

print((math.ceil(V-A/A-B) + 1))
#도착은 무조건 아침에 하니까 마지막 날 아침을 빼면 A-B의 개수만 고려할 수 있어 편해진다.











