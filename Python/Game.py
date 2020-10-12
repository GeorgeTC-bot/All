#//////   A little prgram i made using texts
#/////   Always wanted to make one as a kid
#////   finally know how to do so
#///   Will be my favorite
#//
#/   NAME: THE BOX GAME
#\
#\\
#\\\
#\\\\\
#\\\\\\
#\\\\\\\
#\\\\\\\\



import os

player = [0,0]
player_state = "alive"
end = [9,3]
box = [1,1]
grid = ""


end_line = ""

clear = lambda: os.system('cls')

def MakeGrid(l, b, p, e, h, grd):
    grd = ""
    for y in range(0,l,1):
        a = "\n"
        grd = grd + a
        for x in range(0,b,1):
            
            if(x == player[0] and y == player[1]):
                a = p
                grd = grd + a
            elif(x == box[0] and y == box[1]):
                a = e
                grd = grd + a
            elif(x == end[0] and y == end[1]):
                a = h
                grd = grd + a
            else:
                a = "-"
                grd = grd + a
    return grd


while player_state == "alive":
    clear()
    
    grid = MakeGrid(4,10, "X", "O", "H", grid)
    print(grid)

    if(box == end):
        end_line = "\n\nYOU WIN\n\nWrite 'Restart' to continue"
        break
    
    move = input("\nWASD to move: ")
    
    if(move == "w" and player[1] != 0):
        player[1] -= 1
    elif(move == "a" and player[0] != 0):
        player[0] -= 1
    elif(move == "s" and player[1] != 3):
        player[1] += 1
    elif(move == "d" and player[0] != 9):
        player[0] += 1

    if(player == box):
        if(move == "w" and box[1] != 0):
            box[1] -= 1
        elif(move == "a" and box[0] != 0):
            box[0] -= 1
        elif(move == "s" and box[1] != 3):
            box[1] += 1
        elif(move == "d" and box[0] != 9):
            box[0] += 1
        if(player == box):
            if(move == "w"):
                player[1] += 1;
            elif(move == "a"):
                player[0] += 1;
            elif(move == "s"):
                player[1] -= 1;
            elif(move == "d"):
                player[0] -= 1;

print(end_line)
