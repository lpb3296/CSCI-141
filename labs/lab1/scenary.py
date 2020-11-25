# Liam Barry
# CSCI-141: Lab01
# Turtle Scenary
import turtle

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


def main():
    trunk = int(input('enter a trunk size: '))
    color = input('please enter a color: ')
    maple_tree(trunk, color)


main()