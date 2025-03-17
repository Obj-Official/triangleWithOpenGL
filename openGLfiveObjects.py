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

def draw_star():
    """Draws a small star at the current position."""
    glPushMatrix()
    glScalef(0.5, 0.5, 1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    for i in range(12):
        angle = math.radians(i * 36)
        radius = 1 if i % 2 == 0 else 0.5
        glVertex2f(radius * math.cos(angle), radius * math.sin(angle))
    glEnd()
    glPopMatrix()

def draw_triangle():
    """Draws a small triangle at the current position."""
    glPushMatrix()
    glScalef(0.5, 0.5, 1)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(0.0, 1, 0)
    glEnd()
    glPopMatrix()

def draw_oval():
    """Draws a small oval at the current position."""
    glPushMatrix()
    glScalef(0.6, 0.3, 1)  # Oval shape by scaling differently on x and y
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.5, 0.0)  # Orange
    for i in range(360):
        angle = math.radians(i)
        glVertex2f(math.cos(angle), math.sin(angle))
    glEnd()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3, 3, -2, 2, -1, 1)  # Set 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the shapes spaced out
        glPushMatrix()
        glTranslatef(-2, 1, 0)  # Move circle left
        draw_circle()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-1.5, -1, 0)  # Move square slightly left and down
        draw_square()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 1, 0)  # Move pentagon up
        draw_pentagon()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1.5, -1, 0)  # Move star to the right and down
        draw_triangle()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(2, 1, 0)  # Move oval to the right
        draw_oval()
        glPopMatrix()

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
