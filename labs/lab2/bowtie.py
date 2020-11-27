# Liam Barry
# CSCI-141: lab2
# Recursive bowtie

import turtle

def bowtie(len):
    turtle.right(30)
    turtle.color('blue')
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
    turtle.forward(len/4)
    turtle.left(90)
    turtle.down()

    turtle.color('red')
    turtle.begin_fill()
    turtle.circle(len/4)
    turtle.end_fill()
    turtle.up()

    turtle.right(90)
    turtle.back(len/4)

def rec_bowtie1(len, depth):
    if depth > 0:
        turtle.speed(0)
        print('depth = ' + str(depth))
        bowtie(len)

        turtle.up()
        turtle.left(30)
        turtle.forward(len*2.5)
        turtle.down()

        rec_bowtie1(len/2, depth-1)

        turtle.up()
        turtle.back(len*2.5)
        turtle.right(60)
        turtle.forward(len*2.5)
        turtle.down()

        rec_bowtie1(len/2, depth-1)

        turtle.up()
        turtle.back(len*2.5)
        turtle.left(180)
        turtle.forward(len*2.5)
        turtle.down()

        rec_bowtie1(len/2, depth-1)

        turtle.up()
        turtle.forward(len*2.5)
        turtle.right(120)
        turtle.forward(len*2.5)
        turtle.down()

        rec_bowtie1(len/2, depth-1)

        turtle.up()
        turtle.left(30)
        turtle.forward(len*2.5)
        turtle.right(30)
        turtle.down()
        turtle.down()



# def rec_bowtie2(len):
#     turtle.speed(0)
#     bowtie(len)
#
#     turtle.left(30)
#     turtle.forward(len * 2.5)
#     turtle.right(30)
#     turtle.down()
#
#     rec_bowtie1(len/2)
#
#     turtle.left(30)
#     turtle.back(len * 2.5)
#     turtle.right(60)
#     turtle.forward(len * 2.5)
#     turtle.left(30)
#     turtle.down()
#
#     rec_bowtie1(len/2)
#
#     turtle.right(30)
#     turtle.back(len * 2.5)
#     turtle.left(180)
#     turtle.forward(len * 2.5)
#     turtle.right(150)
#     turtle.down()
#
#     rec_bowtie1(len/2)
#
#     turtle.right(30)
#     turtle.forward(len*2.5)
#     turtle.right(120)
#     turtle.forward(len*2.5)
#     turtle.left(150)
#     turtle.down()
#
#     rec_bowtie1(len/2)
#     turtle.done()


def main():
    len = int(input('please enter a length: '))
    rec_bowtie1(len, 2)

main()