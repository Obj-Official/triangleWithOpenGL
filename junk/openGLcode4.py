import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Global transformation variables
rotation_angle = 0
scale_factor = 1.0

def draw_triangle():
    """Draws a simple colored triangle in 3D."""
    glLoadIdentity()
    glTranslatef(0, 0, -5)  # Move triangle into the scene
    glRotatef(rotation_angle, 0, 0, 1)
    glScalef(scale_factor, scale_factor, scale_factor)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(-0.5, -0.5, 0)
    
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(0.5, -0.5, 0)
    
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(0.0, 0.5, 0)
    
    glEnd()

def draw_button(x, y, width, height):
    """Draws a rectangle button in OpenGL (for overlay UI)."""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.2, 0.2)  # Red color
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def render_text(screen, font, text, x, y):
    """Renders text using Pygame's font system and overlays it."""
    text_surface = font.render(text, True, (255, 255, 255))  # White text
    screen.blit(text_surface, (x, y))

def main():
    global rotation_angle, scale_factor

    pygame.init()
    display = (500, 500)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    font = pygame.font.SysFont("Arial", 24)  # Font for button text

    # OpenGL 3D Setup
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Convert Pygame coordinates to OpenGL overlay coordinates
                mouse_y = 500 - mouse_y  # Flip Y-axis

                if 20 <= mouse_x <= 120 and 20 <= mouse_y <= 60:
                    rotation_angle += 15  # Rotate by 15 degrees
                elif 140 <= mouse_x <= 240 and 20 <= mouse_y <= 60:
                    scale_factor += 0.2  # Scale up

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the 3D Triangle
        draw_triangle()

        # Switch to 2D Mode for UI Rendering
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, 500, 0, 500)  # 2D coordinate system for buttons
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Draw UI Buttons
        draw_button(20, 20, 100, 40)   # Rotate Button
        draw_button(140, 20, 100, 40)  # Scale Button

        # Switch Back to 3D Mode
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

        # Render button text using Pygame (not OpenGL)
        render_text(screen, font, "Rotate", 40, 30)
        render_text(screen, font, "Scale", 160, 30)

        pygame.display.flip()  # Swap buffers

    pygame.quit()

if __name__ == "__main__":
    main()
