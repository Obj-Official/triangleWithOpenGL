import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


global rotation_angle, scale_factor

# Define Triangle Vertices
vertices = [
    [0, 1, 0],   # Top vertex
    [-1, -1, 0], # Bottom-left vertex
    [1, -1, 0]   # Bottom-right vertex
]

rotation_angle = 0
scale_factor = 1.0

# Button Properties
button_rotate = pygame.Rect(20, 20, 100, 40)  # (x, y, width, height)
button_scale = pygame.Rect(140, 20, 100, 40)

def draw_triangle():
    glPushMatrix()
    glRotatef(rotation_angle, 0, 0, 1)  # Apply rotation around Z-axis
    glScalef(scale_factor, scale_factor, scale_factor)  # Apply scaling
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()
    glPopMatrix()

def draw_buttons(screen):
    # button_rotate = pygame.Rect(20, 20, 100, 40)  # (x, y, width, height)
    # button_scale = pygame.Rect(140, 20, 100, 40)
    pygame.draw.rect(screen, (100, 50, 50), button_rotate)  # Red button
    pygame.draw.rect(screen, (50, 200, 50), button_scale)   # Green button
    font = pygame.font.SysFont("Georgia", 30)
    text_rotate = font.render("Rotate", True, (255, 255, 255))
    text_scale = font.render("Scale", True, (255, 255, 255))
    screen.blit(text_rotate, (button_rotate.x + 20, button_rotate.y + 10))
    screen.blit(text_scale, (button_scale.x + 20, button_scale.y + 10))

# Initialize OpenGL Window
pygame.init()
display = (500, 500)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glViewport(0, 0, 500, 500)  # Set viewport size
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)  # Move triangle into view

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if button_rotate.collidepoint(mouse_x, mouse_y):
                rotation_angle += 15  # Rotate by 15 degrees
            elif button_scale.collidepoint(mouse_x, mouse_y):
                scale_factor += 0.2  # Increase size

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_triangle()

    # Draw UI using pygame
    screen_ui = pygame.Surface((500, 500), pygame.SRCALPHA)  # UI overlay
    draw_buttons(screen_ui)
    screen.blit(screen_ui, (0, 0))
    
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
sys.exit()
