
def turn(count,id,a):
    if count%2==0 and id == False:
        print("write id ",end="")
        c,d=map(int,input().split())
        if a[c][d]==".":
            a[c][d]="x"
            print_map(a)
            count=count+1




def print_map(a):
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=" ")
        print()

a=[[".",".","."],[".",".","."],[".",".","."]]

count=2

print("x or 0 ",end="")
b=input()
if b=="x" :
    player=False
elif b=="0" or b=="O" or b=="o":
    player=True
else:
    print("error")
    exit


print_map(a)
turn(count,player,a)