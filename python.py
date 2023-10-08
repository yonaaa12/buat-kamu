import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(10)  # Set the drawing speed

# Draw the stem
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.pensize(5)
flower.left(90)
flower.forward(200)

# Draw the petals
petal_colors = ["red", "orange", "yellow", "pink", "purple"]
for _ in range(36):
    flower.color(petal_colors[_ % 5])
    flower.begin_fill()
    flower.circle(100, 70)
    flower.left(110)
    flower.circle(100, 70)
    flower.end_fill()
    flower.left(10)

# Close the drawing window when clicked
screen.exitonclick()
