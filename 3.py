def print_map(a):
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=" ")
        print()
def turn(count,id,a):
    if count%2==0 and id == False:
        print("write id ",end="")
        c,d=map(int,input().split())
        if a[c][d]==".":
            a[c][d]="x"
            print_map(a)
            count=count+1
    elif count%2!=0 and id == True:
        print("write id ",end="")
        c,d=map(int,input().split())
        if a[c][d]==".":
            a[c][d]="0"
            print_map(a)
            count=count+1
    win(a)
def win(a):
    for i in range(3):
        j=0
        if "0" in a[i]:
            if True:
                if a[i][j]==a[i+1][j+1] and a[i][j]==a[i+2][j+2]:   #по диоганали
                    return "0 win"
                elif a[i][j]==a[i][j+1] and a[i][j]==a[i][j+2]:   #по горизантали
                    return  "0 win"
                elif a[i][j]==a[i+1][j] and a[i][j]==a[i+2][j]:
                    return "0 win"
                else:
                    return
                
                    







a=[[".",".","."],[".","0","."],[".","0","."]]
print_map(a)
print(win(a))



def turn(count,id,a):
    if count%2==0 and id == False:
        print("write id ",end="")
        c,d=map(int,input().split())
        if a[c][d]==".":
            a[c][d]="x"
            print_map(a)
            count=count+1
    elif count%2!=0 and id == True:
        print("write id ",end="")
        c,d=map(int,input().split())
        if a[c][d]==".":
            a[c][d]="0"
            print_map(a)
            count=count+1
    win(a)
    






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