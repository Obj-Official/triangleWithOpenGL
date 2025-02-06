################# Import utilities and initialize global variables#################
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image  # For image loading

# Global transformation variables
rotation_angle = 0
scale_factor = 1.0

# Texture storage
rotate_texture = None
scale_texture = None

def load_texture(image_path):
    """Loads an image and converts it into an OpenGL texture with debugging."""
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")  # Convert to RGBA
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip vertically for OpenGL
        img_data = img.tobytes("raw", "RGBA", 0, -1)

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Upload the texture
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        glBindTexture(GL_TEXTURE_2D, 0)  # Unbind texture

        print(f"Loaded texture {image_path} with ID: {texture_id}")
        return texture_id

    except Exception as e:
        print(f"Error loading texture {image_path}: {e}")
        return None  # Return None if loading fails

def draw_icon(texture_id, x, y, width, height):
    """Draws an icon inside a button using OpenGL texture mapping."""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x, y)  # Bottom-left
    glTexCoord2f(1, 0); glVertex2f(x + width, y)  # Bottom-right
    glTexCoord2f(1, 1); glVertex2f(x + width, y + height)  # Top-right
    glTexCoord2f(0, 1); glVertex2f(x, y + height)  # Top-left
    glEnd()

    glDisable(GL_TEXTURE_2D)

################# Draw Triangle Function #################
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

################# Draw Button (rectangle) function #################
def draw_button(x, y, width, height):
    """Draws a rectangle button in OpenGL (for overlay UI)."""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.2, 0.2)  # Red color
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

########=> Main Function
def main():
    global rotation_angle, scale_factor, rotate_texture, scale_texture

################# Initialize pygame  and set window display size #################
    pygame.init()
    display = (500, 500)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

################# Set viewport and projections #################
    # OpenGL 3D Setup 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Load button icons
    rotate_texture = load_texture("rotate.png")
    scale_texture = load_texture("scale.png")

################# Run the pygame window #################
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

################# Draw the 3D Triangle #################
        draw_triangle()

    ###### Switch to 2D Mode for UI Rendering ######
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, 500, 0, 500)  # 2D coordinate system for buttons
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

################# Draw UI Rectangle Buttons #################
        draw_button(20, 20, 100, 40)   # Rotate Button
        draw_button(140, 20, 100, 40)  # Scale Button

        # Draw Icons Inside Buttons
        draw_icon(rotate_texture, 40, 25, 60, 30)  # Rotate icon
        draw_icon(scale_texture, 160, 25, 60, 30)  # Scale icon

    ###### Switch Back to 3D Mode ######
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

        pygame.display.flip()  # Swap buffers

    pygame.quit()

if __name__ == "__main__":
    main()
