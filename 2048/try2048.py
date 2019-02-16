import random        #导入随机函数
import pygame        #导入pygame游戏模块
import sys           #导入系统模块

#创造一个矩形类   初始化这个类，类的初始属性有行和列
class Square:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col




w = 720    #设定窗口宽度为720
h = 720    #设定窗口高度为720
Row = 4    #设定总行数为4
Col = 4    #设定列数为4

greycolor = (30,30,30)    #设置边框颜色  灰色
textcolor = (0,0,0)       #设置文字颜色  黑色

screen = pygame.display.set_mode((w,h))  #定义屏幕舞台
pygame.display.set_caption("2048")       #设置标题为2048
fps = 20                                 #设置帧率为20
fclock = pygame.time.Clock()             #定义一个时钟变量

text =  pygame.font.Font("C:/Windows/Fonts/simsun.ttc",50)  #载入字体  宋体，同时设置文字大小为50


#初始化 二维列表



#创建一个函数1   transfer   把一个含有0的列表变成一个不含0的列表
#例如  输入为 a = [2,0,0,4]
#      函数输出为 [2,4]
def transfer_nozero_list(list):      #输入为 一个列表，用list指示




#创建一个函数2   sum   计算一个列表中的任意相邻2个数的和
#要求 输入的列表必须是一个非零的列表  如[2,4]   不能是[2,0,4]
#例子 输入为 [4,2] 输出依然是[4,2]
#例子2 输入为[2,2,4] 输出为 [4,4]
#例子3 输入为[2,2,4,4] 输出为 [4,8]
def sum_of_every_2_number(nozerolist):    # 输入为列表    非零列表
    if(len(nozerolist)==0):         #如果列表为空
        return []                   #返回一个空列表
    elif(len(nozerolist)==1):       # 如果列表长度为1
        return nozerolist           # 则返回列表本身
    elif(len(nozerolist)==2):       #如果列表长度为2
        if (nozerolist[0] == nozerolist[1]):        #如果2个值相同
            return [nozerolist[0]+nozerolist[0]]    #返回他们的和，作为一个量，并返回为列表的形式。      例如 [2,2] 返回[4]而不是4
        else:                                       #如果2个值不同
            return nozerolist                       #返回原列表
    if(len(nozerolist)>2):          #如果列表长度大于2，这里要通过递归函数来实现所有相邻数的判断，不清楚递归函数的，需要先理解递归函数
        if(nozerolist[0]==nozerolist[1]):       #如果第一项和第二项相等
            nozerolist[0] = nozerolist[0] +nozerolist[0]        #第一项的值等于，第一项+第二项
            return [nozerolist[0]] + sum_of_every_2_number(nozerolist[2:])  #递归，返回列表[第一项，sum(原列表移除前2项)]
        else:                                   #如果第一项和第二项不相等
            return [nozerolist[0]] + sum_of_every_2_number(nozerolist[1:])  #递归，返回列表 [第一项，sum(原列表移除前1项)]

#创建一个函数3  output 得到一个列表的输出结果
#例子输入为 [2,0,0,4] 输出应该为[2,4,0,0]
#例子输入为 [2,2,0,4] 输出应该为[4,4,0,0]
#例子输入为 [2,2,4,4] 输出应该为[4,8,0,0]
def get_output_list_of_one_list(newlist):



#创建最重要的函数，函数4计算整个二维列表
#输入1 二维列表数据，grid
#输入2 方向   上、下、左、右
# [0,0,0,0]             [0,0,0,0]
# [0,2,0,0]  向下移动   [0,0,0,0]
# [2,0,0,0]    ------    [0,0,0,0]
# [2,2,4,4]             [4,4,4,4]
def cal_grid_value(grid_value,direction):   #输入变量1grid，变量2方向
    output_grid = []                #初始化二维列表
    if(direction == 'left' or direction == 'right'):   #方向是←或者→
        for x in range(4):     #循环取出二维列表的4个列表
            list = grid_value[x]     #4个子列表保存成新的列表 list
            output_list = [0, 0, 0, 0]   #初始化输出新列表
            if (direction == 'left'):       #如果方向为←
                                 #输出二维列表 添加一个项目，项目内容为新列表output_list，循环4次就可以得到完整的二维列表
            elif(direction == 'right'):     #如果方向为→

    elif(direction == 'up' or direction == 'down'):             #如果方向是↑或者↓，这里就需要顺时针或者逆时针旋转90度
        grid_buffer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]     #初始化一个缓冲二维列表
        output_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]     #初始化一个缓冲输出二维列表
        output_grid_buffer = []  #初始化输出列表
        if(direction == 'up'):   #如果方向是↑，就是先把二维列表逆时针旋转90度，然后转化为向←移动，之后再顺时针旋转90度

            # 此处表示逆时针旋转90度，为什么？  自己画图然后写上每个点坐标，分析即可得到


            #这里与←移那部分完全相同
            for x in range(4):
                list = grid_buffer[x]
                output_list = [0, 0, 0, 0]
                output_list = get_output_list_of_one_list(list)
                output_grid_buffer.append(output_list)

            # 此处表示顺时针旋转90度，为什么？  自己画图然后写上每个点坐标，分析即可得到

        else:   #如果方向是↓，就是先把二维列表顺时针旋转90度，然后转化为向←移动，之后再逆时针旋转90度

            # 此处表示顺时针旋转90度，为什么？  自己画图然后写上每个点坐标，分析即可得到

            # 这里与←移那部分完全相同
            for x in range(4):
                list = grid_buffer[x]
                output_list = [0, 0, 0, 0]
                output_list = get_output_list_of_one_list(list)
                output_grid_buffer.append(output_list)
            # 此处表示逆时针旋转90度，为什么？  自己画图然后写上每个点坐标，分析即可得到

    return output_grid    # 返回最后的二维列表


#创建函数5，对于一个存在的表格，在剩余的位置随机生成一个数字，2或者4,2的概率为70%，4的概率为30%
# [0,0,0,0]
# [0,2,0,0]    只能在0的位置出现，不能在已经有数字的位置出现
# [2,0,0,0]       问题1，如何得到70%和30%的概率，非常简单用 random.random()<0.7即可
# [2,2,4,4]       问题2，如何随机位置，非常简单用 int(random.random()*len(list))即可
def create_new_value(grid):  #输入为一个二维列表


#创建绘图函数    绘制一个矩形窗口
#例如  grid（Square（0,1），greycolor,2） 就是在row=0  col=1这个位置，绘制一个边框为灰色的矩形方块， 数字内容为2
#这里的输入有3个参量，square是前面定义的square类，用来确定生成位置的
#  bordercolor 变量为边框的颜色
#  value 是填充数字内容的文字，2 4 8 16 32 64 128 256 512 1024 2048 .......
#   不同value可以设置不同的背景颜色，背景颜色具体设置在函数内
def grid(square,bordercolor,value):


    #这里一大段都是定义颜色，不同数字不同颜色
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




    #文字为一位，两位，三位，四位时候不同的横坐标偏移
    if(value<10):
        leftgap = 10
    elif(value<100):
        leftgap = 20
    elif (value < 1000):
        leftgap = 35
    else:
        leftgap = 50



    pass


#创建更加完整的绘图函数   从一个矩形，绘制出4*4的矩形窗格
#输入只需要二维数组列表
def draw_grid(datalist):




#绘制一个全新的窗口
new_grid = create_new_value(grid_value)

#主程序循环主体
while True:

    #所有的按键事件
    for event in pygame.event.get():    #响应所有的事件
        direction = ''   #初始化方向变量，变量值为空
        if (event.type == pygame.QUIT):  # 接收到退出事件后退出程序
            sys.exit()   #关闭程序
        elif(event.type == pygame.KEYDOWN): #接收到方向键

        else:
            print(event)        #打印所有事件
    # 绘制背景，背景颜色是白色


    #刷新表格外观


    #设置时钟频率
    fclock.tick(fps)
    # 刷新画面
    pygame.display.update()
