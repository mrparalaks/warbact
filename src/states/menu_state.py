import pygame
from src.core.state import State
from src.core.logging_setup import logger

class MenuState(State):
    """Состояние главного меню"""

    def __init__(self, game) -> None:
        super().__init__(game)

        # Загружаем ресурсы
        self.font = self.game.resource_manager.load_font(
            "main_font", "arial.ttf", 36
        )

        # Загружаем текстуры
        self.background = self.game.resource_manager.load_scaled_texture(
            "menu_bg", "background.jpg", 800, 600
        )

        try:
            self.logo = self.game.resource_manager.load_texture(
                "logo", "logo.png"
            )
        except:
            self.logo = None

        try:
            self.button = self.game.resource_manager.load_texture(
                "start_button", "button.png"
            )
            self.button_rect = self.button.get_rect(center=(400, 400))
        except:
            self.button = None

        # Загружаем звуки
        try:
            self.game.resource_manager.load_sound("click", "click.wav")
        except:
            logger.warning("Не удалось загрузить звук click")

        logger.info("Инициализировано состояние MenuState")

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    logger.info("Переход в игровое состояние")
                    try:
                        self.game.resource_manager.play_sound("click")
                    except:
                        pass  # Игнорируем ошибки со звуком
                    from src.states.game_state import GameState
                    self.set_next_state(GameState(self.game))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hasattr(self, 'button') and self.button and self.button_rect.collidepoint(event.pos):
                    logger.info("Переход в игровое состояние (по кнопке)")
                    try:
                        self.game.resource_manager.play_sound("click")
                    except:
                        pass  # Игнорируем ошибки со звуком
                    from src.states.game_state import GameState
                    self.set_next_state(GameState(self.game))

    def render(self, screen) -> None:
        # Отрисовка фона
        screen.blit(self.background, (0, 0))

        # Отрисовка логотипа (если загружен)
        if hasattr(self, 'logo') and self.logo:
            screen.blit(self.logo, (300, 100))

        # Отрисовка кнопки (если загружена)
        if hasattr(self, 'button') and self.button:
            screen.blit(self.button, self.button_rect)

        # Отрисовка текста главного меню
        title = self.font.render("Главное меню", True, (255, 255, 255))
        screen.blit(title, (300, 250))

        # Отрисовка инструкции (если кнопка не загружена)
        if not hasattr(self, 'button') or not self.button:
            instruction = self.font.render("Нажмите Enter для начала игры", True, (255, 255, 255))
            screen.blit(instruction, (200, 300))
