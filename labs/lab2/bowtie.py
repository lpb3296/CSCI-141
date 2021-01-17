# Liam Barry
# CSCI-141: lab2
# Recursive bowtie

import turtle

def bowtie(len):
    turtle.speed(10)
    turtle.color('blue')
    turtle.down()

    turtle.right(30)
    turtle.forward(len)

    turtle.left(120)
    turtle.forward(len)

    turtle.left(120)
    turtle.forward(len*2)

    turtle.right(120)
    turtle.forward(len)

    turtle.right(120)
    turtle.forward(len)

    turtle.left(30)

    turtle.up()
    turtle.forward(len/3)
    turtle.left(90)

    turtle.down()
    turtle.color('red')
    turtle.begin_fill()
    turtle.circle(len/3)
    turtle.end_fill()
    turtle.up()

    turtle.right(90)
    turtle.back(len/3)

def rec_bowtie1(len, depth):
    if depth > 0:
        bowtie(len)

        turtle.up()
        turtle.right(30)
        turtle.forward(len*2)
        turtle.down()

        rec_bowtie1(len/3, depth-1)

        turtle.up()
        turtle.back(len*2)
        turtle.left(30)

        turtle.left(30)
        turtle.forward(len*2)
        turtle.down()

        rec_bowtie1(len/3, depth-1)

        turtle.up()
        turtle.back(len*2)
        turtle.right(60)

        turtle.back(len*2)
        turtle.down()

        rec_bowtie1(len/3, depth-1)

        turtle.up()
        turtle.forward(len*2)
        turtle.left(30)

        turtle.left(30)
        turtle.back(len*2)
        turtle.down()

        rec_bowtie1(len/3, depth-1)

        turtle.up()
        turtle.forward(len*2)
        turtle.right(30)


def main():
    len = int(input('please enter a length: '))
    depth = int(input('please enter a depth: '))
    turtle.setworldcoordinates(-1000, -1000, 1000, 1000)
    rec_bowtie1(len, depth)
    turtle.done()

main()