# Liam Barry
# CSCI-141: hw3
# Circles

import turtle

def circle1(radius, color):
    turtle.color(color)
    turtle.up()
    turtle.forward(radius)
    turtle.left(90)
    turtle.down()

    turtle.circle(radius)
    turtle.up()
    turtle.goto(0,0)

def circle2(radius, color):
    rad = radius / 2
    turtle.color(color)
    turtle.down()
    turtle.circle(rad)
    turtle.right(180)
    turtle.circle(rad)
    turtle.up()
    turtle.goto(0,0)

def circle3(radius, color):
    rad = radius / 4
    turtle.left(90)
    turtle.forward(radius/2)
    turtle.color(color)
    turtle.down()

    turtle.circle(rad)
    turtle.right(180)
    turtle.circle(rad)
    turtle.up()
    turtle.goto(0,0)
    turtle.forward(radius/2)

    turtle.down()
    turtle.circle(rad)
    turtle.right(180)
    turtle.circle(rad)
    turtle.up()
    turtle.goto(0,0)
    turtle.done()

def main():

    while True:
        try:
            amt = int(input('how many layers would you like (1 - 3): '))
            radius = int(input('please enter a radius: '))
            color = input('please enter a color: ')

            if amt == 0:
                print('no circles for you :(')

            if amt == 1:
                circle1(radius, color)
            if amt == 2:
                color2 = input('what would you like the second color to be: ')

                circle1(radius, color)
                circle2(radius, color2)
            if amt == 3:
                color2 = input('what would you like the second color to be: ')
                color3 = input('what would you like the third color to be:  ')

                circle1(radius, color)
                circle2(radius, color2)
                circle3(radius, color3)
            return False

        except turtle.TurtleGraphicsError:
            print('please enter a valid color')

main()