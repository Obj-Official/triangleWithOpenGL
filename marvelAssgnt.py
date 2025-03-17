import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, cos, sin

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glEnd()

def draw_circle():
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(361):
        angle = i * pi / 180
        glVertex2f(cos(angle), sin(angle))
    glEnd()

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(0, 1)
    glEnd()

def draw_hexagon():
    glBegin(GL_POLYGON)
    for i in range(6):
        angle = i * 2 * pi / 6
        glVertex2f(cos(angle), sin(angle))
    glEnd()

def draw_pentagon():
    glBegin(GL_POLYGON)
    for i in range(5):
        angle = i * 2 * pi / 5
        glVertex2f(cos(angle), sin(angle))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(-2, 2, -6)
    draw_square()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2, 2, -6)
    draw_circle()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-2, -2, -6)
    draw_triangle()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2, -2, -6)
    draw_hexagon()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0, -6)
    draw_pentagon()
    glPopMatrix()
    
    pygame.display.flip()

def main():
    pygame.init()
    display_size = (800, 600)
    pygame.display.set_mode(display_size, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display()
    pygame.quit()

if __name__ == "__main__":
    main()