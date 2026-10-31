import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Проект Genesis")

    COLORS = {
        "bg":       (15, 15, 25),
        "text":     (220, 220, 255),
    }
    font = pygame.font.SysFont("Arial", 24)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLORS["bg"])
        text = font.render("Урок 1: окно работает! Закрой меня.", True, COLORS["text"])
        screen.blit(text, (40, 40))

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()


