import pygame
from src.core.state import State
from src.core.logging_setup import logger

class MenuState(State):
    """Состояние главного меню"""

    def __init__(self, game) -> None:
        super().__init__(game)
        self.background = pygame.Surface((800, 600))
        self.background.fill((0, 0, 100))

        # Загружаем ресурсы
        self.font = self.game.resource_manager.load_font(
            "main_font", "arial.ttf", 36
        )

        # Загружаем текстуры (если есть)
        try:
            self.logo = self.game.resource_manager.load_texture(
                "logo", "logo.png"
            )
        except:
            self.logo = None

        logger.info("Инициализировано состояние MenuState")

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    logger.info("Переход в игровое состояние")
                    from src.states.game_state import GameState
                    self.set_next_state(GameState(self.game))

    def render(self, screen) -> None:
        screen.blit(self.background, (0, 0))

        # Отрисовка логотипа (если загружен)
        if self.logo:
            screen.blit(self.logo, (300, 100))

        # Отрисовка текста
        text = self.font.render("Главное меню", True, (255, 255, 255))
        screen.blit(text, (300, 250))

        text = self.font.render("Нажмите Enter для начала игры", True, (255, 255, 255))
        screen.blit(text, (200, 300))
