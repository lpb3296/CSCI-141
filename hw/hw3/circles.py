# Liam Barry
# CSCI-141: hw3
# Circles

import turtle

def circle(radius, color):
    turtle.color(color)
    turtle.up()
    turtle.forward(radius)
    turtle.left(90)
    turtle.down()

    turtle.circle(radius)
    turtle.up()
    turtle.goto(0,0)


def main():

    while True:
        try:
            radius = int(input('please enter a radius: '))
            color = input('please enter a color: ')
            circle(radius, color)
            return False

        except turtle.TurtleGraphicsError:
            print('please enter a valid color')

main()