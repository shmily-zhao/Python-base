#字符串拼接。用户输入两个字符串，将它们组合后输出。
# str1 = input("请输入一个人的名字：")
# str2 = input("请输入一个国家名字：")
# print ("世界这么大，{}想看{}看看。".format(str1,str2))


#整数序列求和。用户输入一个正整数 N，计算从 1 到 N（包含 1和 N）相加之后的结果。
# n =input("请输入整数N：")
# sum = 0
# for i in range(int(n)):
#     sum += i+1
# print ("1到N求和结果：",sum)


#九九乘法表输出。工整打印输出常用的九九乘法表，格式不限。
# for i in range(1,10):
#     for j in range(1,i+1):
#         print ("{}*{}={:2}".format(j,i,i*j),end='  ')
#     print ('')


#阶乘计算。计算 1+2!+3!+...+10!的结果。
# sum,tmp = 0,1
# for i in range(1,5):
#     tmp *= i
#     sum += tmp
# print ("运算结果是:{}".format(sum))


#猴子吃桃问题。猴子第一天摘下若干个桃子，当即吃了一半，还
# 不过瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多
# 吃了一个。以后每天早上都吃了前一天剩下的一半多一个。到第五天
# 早上想再吃时，见只剩下一个桃子了。请编写程序计算猴子第一天共
# 摘了多少桃子。
# n=1
# for i in range(5,0,-1):
#     n = (n+1)<<1
# print (n)


#健康食谱输出。列出 5 种不同的食材，请输出它们可能组成的所
#有菜式名称。
# diet = ['西蓝花','花椰菜','黄瓜','牛排','虾仁']
# count = 0
# for x in range(0,5):
#     for y in range(0,5):
#         print ("{}{}".format(diet[x],diet[y]))
#         count +=1
# print (count)


#五角星的绘制。绘制一个红色的五角星图形，如图所示。
# from turtle import *  #turtle是Python简单的绘图模块
# fillcolor("red")
# begin_fill()
# while True:
#     forward(200)
#     right(144)
#     if abs(pos()) < 1:  #查看画笔是否回到原点
#         break           #如果回到原点，则跳出循环
# end_fill()


#太阳花的绘制。绘制一个太阳花的图形，如图所示。
# from turtle import *
# color('red','yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()


#螺旋线绘制。绘制一个螺旋线的图形，如图所示。
# import  turtle
# import time
# turtle.speed("fastest")
# turtle.pensize(2)
# for x in range(100):
#     turtle.forward(2*x)
#     turtle.left(90)
# time.sleep(3)


#彩色螺旋线的绘制。绘制一个彩色螺旋线，如图所示。
import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue","white","green"]
turtle.tracer(False)
for x in range(600):
    turtle.forward(2*x)
    turtle.color(colors[x %6])
    turtle.left(91)
turtle.tracer(True)
