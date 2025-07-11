import pygame
import sys
from core.logging_setup import setup_logging

# Настройка логирования
logger = setup_logging()

def main():
    logger.info('Инициализация Pygame')
    pygame.init()

    # Настройка окна
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('WarBact')

    # Основной игровой цикл
    clock = pygame.time.Clock()
    running = True

    logger.info('Запуск основного игрового цикла')
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info('Получен сигнал выхода')
                running = False
        
        # Очистка экрана
        screen.fill((0, 0, 0))

        # Здесь будет основная логика игры

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60) # 60 FPS
    
    logger.info('Завершение работы Pygame')
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()