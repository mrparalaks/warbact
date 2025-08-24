import pygame
from src.core.state import State
from src.core.logging_setup import logger

class PauseState(State):
    """Состояние паузы"""

    def __init__(self, game) -> None:
        super().__init__(game)
        self.background = pygame.Surface((800, 600), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 128))  # Полупрозрачный чёрный
        self.font = pygame.font.SysFont('Arial', 36)
        logger.info("Инициализировано состояние PauseState")

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    logger.info("Возвращаемся в игровое состояние")
                    from src.states.game_state import GameState
                    self.set_next_state(GameState(self.game))

    def render(self, screen) -> None:
        # Сначала отрисовываем игровое состояние под паузой
        if hasattr(self.game, 'previous_state') and self.game.previous_state:
            self.game.previous_state.render(screen)

        # Затем отрисовываем полупрозрачный оверлей паузы
        screen.blit(self.background, (0, 0))
        text = self.font.render("Пауза", True, (255, 255, 255))
        screen.blit(text, (350, 250))
        text = self.font.render("Нажмите ESC для продолжения", True, (255, 255, 255))
        screen.blit(text, (180, 300))
