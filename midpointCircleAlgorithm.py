import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_circle(radius):
    """Draws a circle using the Midpoint Circle Algorithm."""
    x, y = 0, radius
    P = 1 - radius  # Initial decision parameter

    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)  # White color

    while x <= y:
        # Plot all 8 symmetric points
        glVertex2f(x, y)
        glVertex2f(y, x)
        glVertex2f(y, -x)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)
        glVertex2f(-y, x)
        glVertex2f(-x, y)

        x += 1
        if P < 0:
            P += 2 * x + 1
        else:
            y -= 1
            P += 2 * (x - y) + 1

    glEnd()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-50, 50, -50, 50)  # Set coordinate system

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)
        draw_circle(20)  # Call function to draw circle with r=20
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
