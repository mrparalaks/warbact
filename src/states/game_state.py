import pygame
from src.core.state import State
from src.core.logging_setup import logger

class GameState(State):
    """Основное игровое состояние"""

    def __init__(self, game) -> None:
        super().__init__(game)
        self.background = pygame.Surface((800, 600))
        self.background.fill((0, 100, 0))
        self.font = pygame.font.SysFont('Arial', 24)
        logger.info("Инициализировано состояние GameState")

    def handle_events(self, events) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    logger.info("Переход в состояние паузы")
                    from src.states.pause_state import PauseState
                    self.set_next_state(PauseState(self.game))

    def render(self, screen) -> None:
        screen.blit(self.background, (0, 0))
        text = self.font.render("Игровое состояние", True, (255, 255, 255))
        screen.blit(text, (300, 250))
        text = self.font.render("Нажмите ESC для паузы", True, (255, 255, 255))
        screen.blit(text, (250, 300))
