# Liam Barry
# CSCI-141: Lab01
# Turtle Scenary
import turtle
import math

"""
make a maple tree with user inputer size and color
"""
def maple_tree(trunk, color):
    top = trunk * .4

    turtle.down()
    turtle.left(90)
    turtle.color(color)
    turtle.forward(trunk)
    turtle.right(90)
    turtle.circle(top)
    turtle.right(90)
    turtle.up()
    turtle.forward(trunk)
    turtle.left(90)

def pine_tree(trunk, color):
    top = trunk * .6

    turtle.down()
    turtle.left(90)
    turtle.color(color)
    turtle.forward(trunk)
    turtle.right(90)
    turtle.forward(top/2)
    turtle.left(120)
    turtle.forward(top)
    turtle.left(120)
    turtle.forward(top)
    turtle.left(120)
    turtle.forward(top/2)
    turtle.up()
    turtle.right(90)
    turtle.forward(trunk)
    turtle.left(90)

def build_house(color):

    turtle.color(color)
    turtle.down()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(71)
    turtle.left(90)
    turtle.forward(71)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.up()

def init():
    turtle.up()
    turtle.goto(-500, -400)
    turtle.down()
    turtle.color('green')
    turtle.forward(1000)
    turtle.up()
    turtle.goto(0, 0)

def main():
    house = input('would you like a house (y/n): ')
    pos = int(input('at which position (1/2/3)?: '))
    color = input('what color?: ')

    turtle.setworldcoordinates(-500, -500, 500, 0)
    init()

    if pos == 1:
        turtle.up()
        turtle.goto(0, -400)
        pine_tree(100, 'green')

        turtle.up()
        turtle.goto(400, -400)
        maple_tree(100, 'green')

        turtle.up()
        turtle.goto(-400, -400)
        turtle.down()

    if pos == 2:
        turtle.up()
        turtle.goto(-400, -400)
        pine_tree(100, 'green')

        turtle.up()
        turtle.goto(400, -400)
        maple_tree(100, 'green')

        turtle.up()
        turtle.goto(0, -400)
        turtle.down()

    if pos == 3:
        turtle.up()
        turtle.goto(-400, -400)
        pine_tree(100, 'green')

        turtle.up()
        turtle.goto(0, -400)
        maple_tree(100, 'green')

        turtle.up()
        turtle.goto(400, -400)

    if house == 'y':
        build_house(color)

main()