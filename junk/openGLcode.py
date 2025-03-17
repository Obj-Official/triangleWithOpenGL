import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global rotation_angle, scale_factor
rotation_angle = 0
scale_factor = 1.0

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen
    glLoadIdentity()  # Reset transformations
    glRotatef(rotation_angle, 0, 0, 1)  # Apply rotation around Z-axis
    glScalef(scale_factor, scale_factor, scale_factor)  # Apply scaling
    
    glBegin(GL_TRIANGLES)  # Start drawing a triangle

    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex3f(-0.5, -0.5, -2.0)  # Bottom left

    glColor3f(0.0, 1.0, 0.0)  # Green color
    glVertex3f(0.5, -0.5, -2.0)  # Bottom right
    
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex3f(0.0, 0.5, -2.0)  # Top center
    glEnd()

    pygame.display.flip()  # Update display

def draw_button(x, y, width, height):
    """Draws a rectangle button in OpenGL."""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.2, 0.2)  # Red color
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def main():
    pygame.init()
    display = (500, 500)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    font = pygame.font.SysFont("Georgia", 30)
    text_rotate = font.render("Rotate", True, (255, 255, 255))
    text_scale = font.render("Scale", True, (255, 255, 255))
    button_rotate = pygame.Rect(20, 20, 100, 40)  # (x, y, width, height)
    button_scale = pygame.Rect(140, 20, 100, 40)

    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    
    glTranslatef(0, 0, -2)  # Move the object back to be visible

    running = True
    while running:
        screen.fill('pink')
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_rotate.collidepoint(mouse_x, mouse_y):
                    rotation_angle += 15  # Rotate by 15 degrees
                    draw()
                elif button_scale.collidepoint(mouse_x, mouse_y):
                    scale_factor += 0.2  # Increase size
                    draw()

        draw()
        # Draw Buttons
        glLoadIdentity()
        draw_button(20, 20, 100, 40)   # Rotate Button
        draw_button(140, 20, 100, 40)  # Scale Button

        # pygame.display.update()  # Swap buffers

    pygame.quit()

if __name__ == "__main__":
    main()
