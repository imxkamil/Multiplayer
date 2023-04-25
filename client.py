import pygame
from network import Network
from player import Player

win = pygame.display.set_mode((500,500)) 


pygame.display.set_caption("Client")


def redrawWindow(win, player, player2):

    win.fill("white")
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    running = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)



main()