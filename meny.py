#meny without pygame library
import pygame

W, H = 900, 600
sc = pygame.display.set_mode((W, H))


#функция главного меню, без библиотеки
def show_menu():
    label = pygame.font.SysFont('arial', 50)
    name_label = label.render('Player1', True, (255, 0, 255))
    name_label_rect = name_label.get_rect(topleft=(150, 150))
    start_label = label.render('Start', True, (255, 0, 255))
    start_label_rect = start_label.get_rect(topleft=(150, 250))
    quit_label = label.render('Quit', True, (255, 0, 255))
    quit_label_rect = quit_label.get_rect(topleft=(150, 350))
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        sc.fill((255, 255, 255))
        sc.blit(name_label, name_label_rect)
        sc.blit(start_label, start_label_rect)
        sc.blit(quit_label, quit_label_rect)

        mouse = pygame.mouse.get_pos()
        if name_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            #funk enter name
            pass

        if start_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            #
            game_play = True
            break

        if quit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            #
            exit()

        pygame.display.update()
