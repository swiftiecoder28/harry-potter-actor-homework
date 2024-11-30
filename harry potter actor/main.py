import pgzrun
import random

WIDTH = 700
HEIGHT = 700

hermione = Actor("harrypotter")
hermione.pos = random.randint(50,600), random.randint(50, 400)

def draw():
    screen.fill("#87CEFA")
    hermione.draw()

def move_hermione():
    hermione.x = random.randint(70, 370)
    hermione.y = random.randint(70, 370)

def on_mouse_down(pos):
    if hermione.collidepoint(pos):
        move_hermione()

    

def update():
    pass

pgzrun.go()