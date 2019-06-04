import turtle
#import是保留字，用来引入一个外部库
#turtle是绘制图像的函数库
def drawSnake(rad,angle,len,neckrad):
    #def定义函数，所定义函数在程序中未经调用不能执行，需要通过函数名调用才能够执行
    for i in range(len):
        turtle.circle(rad,angle)
        #小乌龟严圆形轨迹爬行，
        # 参数rad描述圆形轨迹半径的位置，这个半径在小乌龟运行的左侧rad远位置处，如果rad为负值，则半径在小乌龟运行的右侧
        #参数angle表示小乌龟沿着圆形爬行的弧度值
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    #turtle.fd()函数也可以用turtle.forward()表示乌龟向前直线爬行移动
    #参数表示爬行的距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0)
    #启动一个图形窗口，参数：显示窗口的宽度，高度，在屏幕上的位置
    pythonsize = 30
    turtle.pensize(pythonsize)
    #小乌龟运行轨迹的宽度
    turtle.pencolor("blue")
    #小乌龟运行轨迹的颜色，用rgb定义颜色
    turtle.seth(-40)
    #小乌龟启动时运行轨迹的方向，它包含一个输入参数，是角度值。0，90，180,270分别代表东，北，西，南，负值代表相反的方向
    #我们让小乌龟向-40度启动爬行，即：向东南方向40度。
    drawSnake(40,80,5,pythonsize/2)

main()#程序要执行main函数