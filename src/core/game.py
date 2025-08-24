from typing import List, Optional
import pygame
from src.core.state import State
from src.core.resource_manager import ResourceManager
from src.core.logging_setup import logger

class Game:
    """Менеджер состояний игры"""

    def __init__(self) -> None:
        self.states: List[State] = []
        self.current_state: Optional[State] = None
        self.previous_state: Optional[State] = None
        self.running = True
        self.resource_manager = ResourceManager()
        logger.info("Инициализирован менеджер состояний")
        pygame.mixer.init()
        logger.info("Инициализирован микшер звука")

    def quit(self) -> None:
        """Завершение работы игры"""
        if self.running:
            self.running = False
            logger.info("Запрос на завершение игры")

    def change_state(self, state: State) -> None:
        """Изменение текущего состояния"""
        # Проверяем, есть ли текущее состояние
        if self.current_state is not None:
            self.current_state.exit()

        # Устанавливаем предыдущее состояние
        self.previous_state = self.current_state

        # Устанавливаем новое состояние
        self.current_state = state

        # Вызываем метод входа в состояние
        self.current_state.enter()

        # Добавляем состояние в историю
        self.states.append(state)

        logger.info(f"Изменено состояние на: {state.__class__.__name__}")

    def handle_events(self, events: List[pygame.event.Event]) -> None:
        """Обработка событий"""
        if self.current_state:
            self.current_state.handle_events(events)

            if self.current_state.next_state:
                self.change_state(self.current_state.next_state)

    def update(self) -> None:
        """Обновление текущего состояния"""
        if self.current_state:
            self.current_state.update()

    def render(self, screen: pygame.Surface) -> None:
        """Отрисовка текущего состояния"""
        if self.current_state:
            self.current_state.render(screen)

    def run(self) -> None:
        """Основной игровой цикл"""
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("WarBact")
        clock = pygame.time.Clock()

        # Начинаем с состояния главного меню
        from src.states.menu_state import MenuState
        self.change_state(MenuState(self))

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()
                    break
            
            if not self.running:
                break

            self.handle_events(events)
            self.update()
            self.render(screen)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
