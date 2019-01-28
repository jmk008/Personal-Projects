from sense_hat import SenseHat
from time import sleep

#check wall
def check_wall(new_x,new_y,x,y):
    if maze[new_y][new_x] != r:
        return new_x,new_y
    elif maze[new_y][x] != r:
        return x,new_y
    elif maze[y][new_x] != r:
        return new_x,y
    else:
        return x,y

#move marble function
def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y

    #left-right movement
    if 1 < pitch < 179 and x!=0:
        new_x -= 1
        
    elif 181 < pitch < 359 and x!=7:
        new_x += 1

    #up-down movement
    if 1 < roll < 179 and y!=7:
        new_y += 1
        
    elif 181 < roll < 359 and y!=0:
        new_y -= 1
        
    new_x,new_y = check_wall(new_x,new_y,x,y)
    return new_x, new_y

#Getting sensehat object
sense = SenseHat()

#clearing the screen
sense.clear()

#wall colors: r for red walls and b for blank, w for while marble, g for green win!
r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,128,0)

#2-d list for rows and columns
#1-d list possible but we need to access rows and columns seperately
maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,g,b,b,r],
        [r,r,r,r,r,r,r,r]]

#initializing marble position
x = 1
y = 1

#game over variable
game_over = False

while not game_over:
    
    #device orientation
    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll = orientation["roll"]

    x,y = move_marble(pitch,roll,x,y)
    #print("pitch {0} roll {1}".format(pitch, roll))

    #winning condition
    if maze[y][x] == g:
        sense.show_message("You Win!")
        game_over = True
        
    #Caution: look carefully its maze[y][x] and not maze[x][y]
    maze[y][x] = w
    #setting pixels, converting 2-d maze to 1-d, since set_pixels takes 1-d list
    sense.set_pixels(sum(maze,[]))

    #Pause program to and reset the previous marble position to blank
    sleep(0.05)
    maze[y][x] = b

