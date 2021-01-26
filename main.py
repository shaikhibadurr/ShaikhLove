import turtle
pen=turtle.Turtle()
def txt():  
    pen.up() 
    pen.setpos(-22, 35)  
    pen.down() 
    pen.color('black')  
    pen.write("Just \n for \nYou", font=("Helvetica", 18, "bold")) 



pen.color("red")
pen.begin_fill()
pen.left(770)
pen.forward(96)
pen.circle(40,180)
pen.end_fill()
pen.left(260)
pen.circle(40,180)
pen.forward(96)

pen.left(220)

txt()
pen.ht() 
