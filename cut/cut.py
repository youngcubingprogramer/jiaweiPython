import random        #导入随机函数
import pygame        #导入pygame游戏模块
import sys           #导入系统模块
from PIL import Image

image = Image.open('1.png')
smallW,smallH = image.size

# 生成一个黑底画面
img_16 = Image.new(image.mode,(smallW,smallH),color='black')
img_16.save('16.png','PNG')


pygame.init()    #初始化pygame
w = 4*smallW+10    #设定窗口宽度为720
h = 4*smallH+10    #设定窗口高度为720
Row = 4    #设定总行数为4
Col = 4    #设定列数为4

greycolor = (30,30,30)    #设置边框颜色  灰色

screen = pygame.display.set_mode((w,h))  #定义屏幕舞台
pygame.display.set_caption("拼图")       #设置标题为2048
fps = 20                                 #设置帧率为20
fclock = pygame.time.Clock()             #定义一个时钟变量

puzzle_1 = pygame.image.load("1.png").convert_alpha()
puzzle_2 = pygame.image.load("2.png").convert_alpha()
puzzle_3 = pygame.image.load("3.png").convert_alpha()
puzzle_4 = pygame.image.load("4.png").convert_alpha()
puzzle_5 = pygame.image.load("5.png").convert_alpha()
puzzle_6 = pygame.image.load("6.png").convert_alpha()
puzzle_7 = pygame.image.load("7.png").convert_alpha()
puzzle_8 = pygame.image.load("8.png").convert_alpha()
puzzle_9 = pygame.image.load("9.png").convert_alpha()
puzzle_10 = pygame.image.load("10.png").convert_alpha()
puzzle_11 = pygame.image.load("11.png").convert_alpha()
puzzle_12 = pygame.image.load("12.png").convert_alpha()
puzzle_13 = pygame.image.load("13.png").convert_alpha()
puzzle_14 = pygame.image.load("14.png").convert_alpha()
puzzle_15 = pygame.image.load("15.png").convert_alpha()
puzzle_16 = pygame.image.load("16.png").convert_alpha()



def randommix(num):
    direct = ['up','down','left','right']
    out = []
    for i in range(num):
        x = int(random.random()*4)
        out.append(direct[x])
    return out


output = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def mix():
    dirlist = randommix(50000)
    print(dirlist)
    for dir in dirlist:
        oldpos = blackpos
        oldnum = 4 * oldpos[1] + oldpos[0]
        newpos = moveblack(dir, blackpos)
        newnum = 4 * newpos[1] + newpos[0]
        output[oldnum], output[newnum] = output[newnum], output[oldnum]
        print(blackpos)

# for i in range(15):
#     x = int(random.random()*len(list))
#     output.append(list[x])
#     list.pop(x)
# output.append(16)
# print(output)


def draw():
    for row in range(0,4):
        for col in range(0,4):
            puzzleName = str(output[4 * col + row])
            puzzleX = smallW * row
            puzzleY = smallH * col
            screen.blit(eval('puzzle_' + puzzleName), (puzzleX,puzzleY))
            pygame.draw.rect(screen, (255,255,255), (puzzleX, puzzleY, smallW, smallH), 3)  # 绘制边框
def moveblack(direction,blackpos):
    if(direction == 'up'):
        if(blackpos[1] !=3):
            blackpos[1] = blackpos[1] + 1
    elif(direction == 'down'):
        if(blackpos[1] !=0):
            blackpos[1] = blackpos[1] - 1
    elif (direction == 'left'):
        if (blackpos[0] != 3):
            blackpos[0] = blackpos[0] + 1
    elif (direction == 'right'):
        if (blackpos[0] != 0):
            blackpos[0] = blackpos[0] - 1
    else:
        return false
    return blackpos
#主程序循环主体


blackpos = [3,3]
mix()
draw()
while True:
    #所有的按键事件
    for event in pygame.event.get():    #响应所有的事件
        direction = ''   #初始化方向变量，变量值为空
        if (event.type == pygame.QUIT):  # 接收到退出事件后退出程序
            sys.exit()   #关闭程序
        elif(event.type == pygame.KEYDOWN): #接收到方向键
            if (event.key ==pygame.K_LEFT):  #如果方向键←被按下
                direction = 'left'   #设定方向为←
            elif(event.key == pygame.K_RIGHT):#如果方向键→被按下
                direction = 'right'  #设定方向为→
            elif (event.key == pygame.K_UP):#如果方向键↑被按下
                direction = 'up'    #设定方向为↑
            elif (event.key == pygame.K_DOWN):#如果方向键↓被按下
                direction = 'down'  #设定方向为↓
            else:   #其他按键被按下
                direction = 'unknown'   #设定方向为不知道
            if(direction!= '' and direction!= 'unknown'):  #如果方向   不为空，也不为不知道，那就一定是上下左右被按下了
                oldpos = blackpos
                oldnum = 4 * oldpos[1] + oldpos[0]
                newpos = moveblack(direction, blackpos)
                newnum = 4 * newpos[1] + newpos[0]
                output[oldnum], output[newnum] = output[newnum], output[oldnum]
                draw()


        else:
            print(event)        #打印所有事件
    # 绘制背景，背景颜色是白色
    # pygame.draw.rect(screen,(255,255,255),(0,0,w,h))

    #刷新表格外观
    # draw_grid(new_grid)

    #设置时钟频率
    fclock.tick(fps)
    # 刷新画面
    pygame.display.update()
