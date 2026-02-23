#Michael Graham
#2/22/2026
#This program prints "hello world" 100 times
for i in range(100):
    print("Hello World")


#This program will print each number on a new line.
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in numbers:
    print(num)

#adding square roots
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in numbers:
    print(f"Number: {num}, Square: {num**2}")

#draw a polygon
import turtle

#ask user for polygon details
sides = int(input("Enter polygon sides: "))
length = int(input("Enter each side's length: "))
line_color = input("Enter the color of the line: ")
fill_color = input("Enter the fill color: ")

#set up turtle
t = turtle.Turtle()
t.color(line_color, fill_color)  # Set line and fill colors

#fill polygon
t.begin_fill()

#draw polygon
for _ in range(sides):
    t.forward(length)
    t.right(360 / sides)

#finish
t.end_fill()
t.hideturtle()
turtle.done()

#this program iterates numbers from 1-50 and clarifies divisibility
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)


#this program will draw the sun
import turtle

screen = turtle.Screen()

#create turtle
t = turtle.Turtle()
t.speed(10) 
t.color("yellow")

#draw the sun (circle)
t.penup()
t.goto(0, -50) 
t.pendown()
t.begin_fill()
t.circle(50) 
t.end_fill()
t.penup()
t.goto(0,0)  
t.pendown()

for _ in range(36):  
    t.penup()
    t.forward(50)  
    t.pendown()
    t.forward(30)  
    t.penup()
    t.backward(80)  
    t.right(10)     

t.hideturtle()
turtle.done()
