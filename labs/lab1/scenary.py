# Liam Barry
# CSCI-141: Lab01
# Turtle Scenary
import turtle

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
    turtle.done()

def main():
    trunk = int(input('enter a trunk size: '))
    color = input('please enter a color: ')
    pine_tree(trunk, color)


main()