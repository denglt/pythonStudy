import pygame

pygame.init()

screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    clock.tick(FPS)  # 1s最多更新FPS次画面

    # 取得输入
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏

    # 画面显示
    screen.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
