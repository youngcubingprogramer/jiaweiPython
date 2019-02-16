import random
import pygame
import sys
import os


class Square:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col

pygame.init()
pygame.mixer.init()
pygame.time.delay(1000)
pygame.mixer.music.load("bgm.mp3")  #载入背景音乐
s = pygame.mixer.Sound("biu.wav")  # 载入biu
pygame.mixer.music.play(-1)   #循环播放


w = 720
h = 720
Row = 4
Col = 4

greycolor = (30,30,30)
textcolor = (0,0,0)

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("2048")
fps = 20
fclock = pygame.time.Clock()
text =  pygame.font.Font("C:/Windows/Fonts/simsun.ttc",50)

grid_value = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def transfer_nozero_list(list):
    if(len(list)):
        newlist = []
        for ele in list:
            if(ele!=0):
                newlist.append(ele)
        return newlist
    else:
        return []

def sum_of_every_2_number(nozerolist):
    if(len(nozerolist)==0):
        return []
    elif(len(nozerolist)==1):
        return nozerolist
    elif(len(nozerolist)==2):
        if (nozerolist[0] == nozerolist[1]):
            return [nozerolist[0]+nozerolist[0]]
        else:
            return nozerolist
    if(len(nozerolist)>2):
        if(nozerolist[0]==nozerolist[1]):
            nozerolist[0] = nozerolist[0] +nozerolist[0]
            return [nozerolist[0]] + sum_of_every_2_number(nozerolist[2:])
        else:
            return [nozerolist[0]] + sum_of_every_2_number(nozerolist[1:])

def get_output_list_of_one_list(newlist):
    output_list = [0,0,0,0]
    if (len(newlist) != 0):
        if (len(transfer_nozero_list(newlist)) != 0):
            output = sum_of_every_2_number(transfer_nozero_list(newlist))
            for i in range(len(output)):
                output_list[i] += output[i]
    return output_list

def cal_grid_value(grid_value,direction):
    output_grid = []
    if(direction == 'left' or direction == 'right'):
        for x in range(4):
            list = grid_value[x]
            output_list = [0, 0, 0, 0]
            if (direction == 'left'):
                output_list = get_output_list_of_one_list(list)
                output_grid.append(output_list)
            elif(direction == 'right'):
                newlist = list.copy()
                newlist.reverse()
                output_list = get_output_list_of_one_list(newlist)
                output_list.reverse()
                output_grid.append(output_list)
    elif(direction == 'up' or direction == 'down'):
        grid_buffer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        output_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        output_grid_buffer = []
        if(direction == 'up'):
            for x in range(4):
                for y in range(4):
                    grid_buffer[x][y] = grid_value[y][3-x]
            for x in range(4):
                list = grid_buffer[x]
                output_list = [0, 0, 0, 0]
                output_list = get_output_list_of_one_list(list)
                output_grid_buffer.append(output_list)
            for x in range(4):
                for y in range(4):
                    output_grid[x][y] = output_grid_buffer[3-y][x]
        else:
            for x in range(4):
                for y in range(4):
                    grid_buffer[x][y] = grid_value[3-y][x]
            for x in range(4):
                list = grid_buffer[x]
                output_list = [0, 0, 0, 0]
                output_list = get_output_list_of_one_list(list)
                output_grid_buffer.append(output_list)
            for x in range(4):
                for y in range(4):
                    output_grid[x][y] = output_grid_buffer[y][3-x]
    return output_grid

def create_new_value(grid):
    zero_position_list = []
    for x in range(4):
        for y in range(4):
            if(grid[x][y]==0):
                zero_position_list.append([x,y])
    position = int(random.random()*len(zero_position_list))
    value = 4 if(random.random()>0.7) else 2
    grid[zero_position_list[position][0]][zero_position_list[position][1]] = value
    return grid

def grid(square,bordercolor,value):
    cell_width = w/Col
    cell_height = h/Row
    left = square.col*cell_width
    top = square.row*cell_height
    bgcolor = (255,255,255)
    if(value==0):
        bgcolor = (255,255,255)
    elif(value==2):
        bgcolor = (	255, 182, 193)   #Lemon
    elif (value == 4):
        bgcolor = (	0,191,255)  #SkyBlue
    elif (value == 8):
        bgcolor = (0,255,127)  # SpringGreen
    elif (value == 16):
        bgcolor = (	255,215,0)  # Gold
    elif (value == 32):
        bgcolor = (255,127,80)  # Coral
    elif (value == 64):
        bgcolor = (65,105,225)  # RoyalBlue
    elif (value == 128):
        bgcolor = (238,130,238)  # 紫罗兰
    elif (value == 256):
        bgcolor = (95,158,160)  # 军校蓝
    elif (value == 512):
        bgcolor = (255,140,0)  # DarkOrange
    elif (value == 1024):
        bgcolor = (255, 182, 193)  # pink
    elif (value == 2048):
        bgcolor = (	0,206,209)  # 绿宝石
    else:
        bgcolor = (200, 200, 200)  # grey
    pygame.draw.rect(screen,bordercolor,(left,top,cell_width,cell_height),2)
    pygame.draw.rect(screen,bgcolor,(left+2,top+2,cell_width-3,cell_height-3),0)
    text_ft = text.render(str(value), 1, textcolor)
    if(value<10):
        leftgap = 10
    elif(value<100):
        leftgap = 20
    elif (value < 1000):
        leftgap = 35
    else:
        leftgap = 50
    screen.blit(text_ft, (left+int(cell_width/2)-leftgap, top+int(cell_height/2)-20))
    pass

def draw_grid(datalist):
    for row in range(4):
        for col in range(4):
            grid(Square(row,col),greycolor,datalist[row][col])

new_grid = create_new_value(grid_value)

while True:
    for event in pygame.event.get():
        direction = ''
        if (event.type == pygame.QUIT):  # 接收到退出事件后退出程序
            sys.exit()
        elif(event.type == pygame.KEYDOWN): #接收到方向键
            if (event.key ==pygame.K_LEFT):
                direction = 'left'
            elif(event.key == pygame.K_RIGHT):
                direction = 'right'
            elif (event.key == pygame.K_UP):
                direction = 'up'
            elif (event.key == pygame.K_DOWN):
                direction = 'down'
            else:
                direction = 'unknown'
            if(direction!= '' and direction!= 'unknown'):

                s.play()  # 播放1次
                new_grid_buffer = cal_grid_value(new_grid, direction)
                if (new_grid == new_grid_buffer):
                    draw_grid(new_grid)
                else:
                    new_grid = create_new_value(new_grid_buffer)
                    draw_grid(new_grid)
        else:
            print(event)
    # background
    pygame.draw.rect(screen,(255,255,255),(0,0,w,h))
    # pygame.draw.rect(screen, (55, 200, 5), (100, 100, 200, 200), 0)
    # pygame.draw.rect(screen, (55, 200, 5), (250, 200, 300, 350), 4)
    draw_grid(new_grid)
    fclock.tick(fps)

    # 刷新画面
    pygame.display.update()
