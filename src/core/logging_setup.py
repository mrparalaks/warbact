import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    '''
    Настройка системы логирования
    '''

    logger = logging.getLogger('WarBact')
    logger.setLevel(logging.DEBUG)

    # Создаем папку для логов, если её нет
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Настройка обработчика для файла
    file_handler = RotatingFileHandler(
        'logs/game.log',
        maxBytes=1024*1024,
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)

    # Настройка обработчика для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Форматтер
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавление обработчиков
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Создаем экземпляр логгера
logger = setup_logging()