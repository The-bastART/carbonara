import math
min=0
day=0
hour=0
for d in range(7,8):
    day=day+10
    for h in range(0,1):
        hour=hour+10
        for m in range(-2,3):
            min=min+10
            print(round(math.sin(10*min)*10,2))