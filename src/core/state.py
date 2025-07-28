import pygame
from typing import List, Any, Optional
from src.core.logging_setup import logger


class State:
    '''Базовый класс для всех состояний игры'''

    def __init__(self, game: Any):
        '''
        Инициалиация состояния

        Args:
            game: Ссылка на основной объект игры
        '''
        self.game = game
        self.next_state: Optional['State'] = None
        self._update_counter = 0 # Счётчик для ограничения логирования
        logger.debug(f'Инициализировано состояние: {self.__class__.__name__}')
        

    def handle_events(self, events: List[pygame.event.Event]) -> None:
        '''
        Обработка событий в текущем состоянии

        Args:
            events: Список событий Pygame
        '''
        for event in events:
            if event.type == pygame.QUIT:
                logger.info('Получен сигнал выхода из игры')
                self.game.quit()

    def update(self) -> None:
        '''
        Обновление состояния. Вызвается каждый кадр.
        Логируем только кажыде 60 кадров (примерно раз в секунду)
        '''
        self._update_counter += 1
        if self._update_counter >= 60: # Логируем раз в секунду
            logger.debug(f'Обновление состояния: {self.__class__.__name__}')
            self._update_counter = 0

    def render(self, screen: pygame.Surface) -> None:
        '''
        Отрисовка состояния

        Args:
            screen: Поверхность Pygame для отрисовки
        '''
        pass
    
    def enter(self) -> None:
        '''
        Действие при входе в состояния
        '''
        logger.info(f'Вход в состояние: {self.__class__.__name__}')

    def exit(self) -> None:
        '''
        Действие при выходе из состояния
        '''
        logger.info(f'Вsход из состояние: {self.__class__.__name__}')

    def set_next_state(self, state: 'State') -> None:
        '''
        Установке следующего состояния

        Args:
            state: Следующее состояние
        '''
        self.next_state = state
        logger.debug(f'Устанвлено следующее состояние: {state.__class__.__name__}')