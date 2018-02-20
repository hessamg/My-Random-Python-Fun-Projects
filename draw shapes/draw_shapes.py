import turtle

def draw_square(shape):
        for i in range(4):
            shape.forward(100)
            shape.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.color("purple")
    jeff.speed(15)
    for i in range(36):
        draw_square(jeff)
        jeff.right(10)
    

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.speed(2)
    #angie.circle(50)
    
    window.exitonclick()
    
draw_art()
