import sys
import os
from src.core.game import Game
from src.core.logging_setup import logger

def main() -> None:
    """Основная функция запуска игры"""
    logger.info("Запуск игры")
    game = Game()
    game.run()

if __name__ == "__main__":
    # Добавляем корневую папку проекта в Python path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    main()
