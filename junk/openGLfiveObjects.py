import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_circle():
    """Draws a small circle at the current position."""
    glPushMatrix()
    glScalef(0.5, 0.5, 1)  # Scale down to 1/4 size
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)  # Red
    for i in range(360):
        angle = math.radians(i)
        glVertex2f(math.cos(angle), math.sin(angle))
    glEnd()
    glPopMatrix()

def draw_square():
    """Draws a small square at the current position."""
    glPushMatrix()
    glScalef(0.5, 0.5, 1)  # Scale down to 1/4 size
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glEnd()
    glPopMatrix()

def draw_pentagon():
    """Draws a small pentagon at the current position."""
    glPushMatrix()
    glScalef(0.5, 0.5, 1)  # Scale down to 1/4 size
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    for i in range(5):
        angle = math.radians(i * 72)
        glVertex2f(math.cos(angle), math.sin(angle))
    glEnd()
    glPopMatrix()

def main():
    pygame.init()
    display = (600, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -1, 1, -1, 1)  # Set 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the shapes spaced out
        glPushMatrix()
        glTranslatef(-1.5, 0, 0)  # Move circle left
        draw_circle()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0, 0)  # Centered square
        draw_square()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1.5, 0, 0)  # Move pentagon right
        draw_pentagon()
        glPopMatrix()

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
