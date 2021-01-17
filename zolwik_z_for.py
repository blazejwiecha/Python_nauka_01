import turtle as t # turtle.py
window = t.Screen() # okno programu
turtle = t.Turtle() # element na którym rysujemy
turtle.hideturtle() # usuwa strzałkę
for i in range(4):
    t.forward(150)
    t.left(90)
window.mainloop()
