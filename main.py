from src.core.game import Game
from src.core.logging_setup import logger

def test_resources(game):
    """Тестовая функция для проверки загрузки ресурсов"""
    logger.info("Тестирование загрузки ресурсов...")

    # Тест загрузки текстуры
    try:
        texture = game.resource_manager.load_texture("test_tex", "logo.png")
        logger.info(f"Текстура загружена: {texture.get_width()}x{texture.get_height()}")
    except Exception as e:
        logger.error(f"Ошибка загрузки текстуры: {e}")

    # Тест загрузки шрифта
    try:
        font = game.resource_manager.load_font("test_font", "arial.ttf", 24)
        logger.info(f"Шрифт загружен: {font.get_height()}px")
    except Exception as e:
        logger.error(f"Ошибка загрузки шрифта: {e}")

def main() -> None:
    """Основная функция запуска игры"""
    logger.info("Запуск игры")

    # Инициализируем Pygame перед созданием Game
    pygame.init()

    game = Game()

    # Тестируем загрузку ресурсов
    test_resources(game)

    # Запускаем игру
    game.run()

if __name__ == "__main__":
    import sys
    import os
    import pygame  # Добавляем импорт
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    main()
