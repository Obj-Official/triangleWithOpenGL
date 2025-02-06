import pygame
pygame.init()
display = (500, 500)
screen = pygame.display.set_mode(display)
while True:
    screen.fill('pink')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()