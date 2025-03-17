import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, cos, sin

def draw_cube():
    vertices = [
        [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],
        [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1]
    ]
    edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_pyramid():
    vertices = [(0,1,0), (-1,-1,-1), (1,-1,-1), (1,-1,1), (-1,-1,1)]
    faces = [(0,1,2), (0,2,3), (0,3,4), (0,4,1), (1,2,3,4)]
    glBegin(GL_TRIANGLES)
    for face in faces[:-1]:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_QUADS)
    for vertex in faces[-1]:
        glVertex3fv(vertices[vertex])
    glEnd()

def draw_sphere():
    quadric = gluNewQuadric()
    gluSphere(quadric, 1, 30, 30)

def draw_cylinder():
    quadric = gluNewQuadric()
    gluCylinder(quadric, 1, 1, 2, 30, 30)

def draw_cone():
    quadric = gluNewQuadric()
    gluCylinder(quadric, 1, 0, 2, 30, 30)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(-2, 0, -6)
    draw_cube()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2, 0, -6)
    draw_pyramid()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-2, -2, -6)
    draw_sphere()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2, -2, -6)
    draw_cylinder()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 2, -6)
    draw_cone()
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
