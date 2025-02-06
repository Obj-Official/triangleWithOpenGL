import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def setup():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)  
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)  # Enable depth test

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()  

    glBegin(GL_TRIANGLES)  
    glColor3f(1.0, 0.0, 0.0)  
    glVertex3f(-0.5, -0.5, -2.0)  
    glColor3f(0.0, 1.0, 0.0)  
    glVertex3f(0.5, -0.5, -2.0)  
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(0.0, 0.5, -2.0)  
    glEnd()

    pygame.display.flip()

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

setup()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    pygame.time.wait(10)  

pygame.quit()
