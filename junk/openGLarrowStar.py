import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_arrow():
    """Draws an arrow at the current position."""
    glPushMatrix()
    glScalef(0.2, 0.2, 1)  # Scale down
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(-1.5, -0.5)  # Left base
    glVertex2f(1.5, -0.5)   # Right base
    glVertex2f(1.5, 0.5)    # Right top
    glVertex2f(2.5, 0.5)    # Arrow right tip
    glVertex2f(0, 2.0)      # Arrow head
    glVertex2f(-2.5, 0.5)   # Arrow left tip
    glVertex2f(-1.5, 0.5)   # Left top
    glEnd()
    glPopMatrix()

def draw_star():
    """Draws a star at the current position."""
    glPushMatrix()
    glScalef(0.2, 0.2, 1)  # Scale down
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    points = []
    for i in range(10):  # Create star points
        angle = math.radians(i * 36)  # 360/10 = 36 degrees per point
        radius = 1 if i % 2 == 0 else 0.4  # Alternate between outer and inner points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))
    
    for x, y in points:
        glVertex2f(x, y)

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

        # Draw Arrow
        glPushMatrix()
        glTranslatef(-1.0, 0, 0)  # Move left
        draw_arrow()
        glPopMatrix()

        # Draw Star
        glPushMatrix()
        glTranslatef(1.0, 0, 0)  # Move right
        draw_star()
        glPopMatrix()

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
