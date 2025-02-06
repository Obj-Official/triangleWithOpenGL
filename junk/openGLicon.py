import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image  # For image processing

# Global Variables
texture_id = None

def load_texture(image_path):
    """Loads an image and converts it into an OpenGL texture."""
    global texture_id
    img = Image.open(image_path)
    img = img.convert("RGBA")  # Convert to RGBA format
    img_data = img.tobytes("raw", "RGBA", 0, -1)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Upload the texture to OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glBindTexture(GL_TEXTURE_2D, 0)  # Unbind the texture

def draw_textured_quad():
    """Draws a quad (rectangle) with the texture applied."""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -3)  # Bottom-left
    glTexCoord2f(1, 0); glVertex3f(1, -1, -3)   # Bottom-right
    glTexCoord2f(1, 1); glVertex3f(1, 1, -3)    # Top-right
    glTexCoord2f(0, 1); glVertex3f(-1, 1, -3)   # Top-left
    glEnd()

    glDisable(GL_TEXTURE_2D)

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    load_texture("inc.png")  # Load the image file

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_textured_quad()  # Draw the icon as a texture
        
        pygame.display.flip()  # Swap buffers

    pygame.quit()

if __name__ == "__main__":
    main()
