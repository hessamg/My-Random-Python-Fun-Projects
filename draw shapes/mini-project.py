import turtle

def draw_square(shape):
        for i in range(3):
            shape.forward(50)
            shape.right(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.color("purple")
    jeff.speed(5)
    for i in range(5):
        draw_square(jeff)
        jeff.left(120)
    

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.speed(2)
    #angie.circle(50)
    
    window.exitonclick()
    
draw_art()
