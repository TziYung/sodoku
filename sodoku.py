import random
import numpy
d=0
def check(soduck):
    global error,d
    line=len(soduck)
    newrow=[]
    avoid=set()
    for a in range(9):
        num=[n for n in range(1,10)]
        avoid.clear()
        for b in range(line):
            avoid.add(soduck[b][a])
        for b in range(int(line/3)*3,line):
            for c in range(int(a/3)*3,int(a/3)*3+3):
                avoid.add(soduck[b][c])
        for b in newrow:
            avoid.add(b)
        for b in avoid:
            num.remove(b)
        if len(num):
            newrow.append(random.choice(num))
        else:
            break
    if len(newrow)==9:
        error=0
        soduck.append(newrow)
    else:
        if error >30:
            error=0
            del soduck[-1]
            check(soduck)
            check(soduck)
        else:
            error+=1
            check(soduck)
num=[n for n in range(1,10)]
random.shuffle(num)
error=0
soduck=[]
soduck.append(num)
for _ in range(8):
    check(soduck)
    print('a')
print(numpy.array(soduck))
