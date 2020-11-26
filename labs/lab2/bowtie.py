# Liam Barry
# CSCI-141: lab2
# Recursive bowtie

import turtle

def bow_tie(len):
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

    turtle.right(90)
    turtle.back(len/4)
    turtle.done()

def main():
    len = int(input('please enter a length: '))
    bow_tie(len)

main()