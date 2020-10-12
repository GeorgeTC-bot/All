
player = [0,0]
end = [10,10]

for( x = 0 ; x <= end[0]; x += 1):
    for( y = 0 ; y <= end[0]; y += 1):
        if(x == player[0] && y == player[1]):
            print("X")
        else:
            print("-")
    print(\n)


