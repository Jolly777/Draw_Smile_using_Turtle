#!/usr/bin/env python
# coding: utf-8

# In[1]:


#drawing_smile_using_turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.shape("turtle")
t.setpos(0,0)
t.pendown()
t.pencolor("yellow")
t.pensize("5")
t.speed(3)
t.fillcolor("yellow")
t.begin_fill()
t.circle(130)
t.end_fill()
t.penup()
t.goto(-50,150)
t.pendown()
t.pensize(3)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(50,150)
t.pendown()
t.pensize(3)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(-110,120)
t.pendown()
t.pensize(8)
t.pencolor("black")
t.circle(30,20)
t.rt(100)
t.circle(100,160)
t.rt(90)
t.fd(8)
t.penup()
t.goto(0,12)
t.write("KEEP_SMILING", align="CENTER", font=("Verdana", 12, "bold"))
t.penup()
t.hideturtle()
wn.exitonclick()


# In[ ]:




