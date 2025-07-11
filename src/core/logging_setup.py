import logging
import logging.handlers
import os

def setup_logging():
    '''Конфигурация логирования
    '''
    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)

    logger = logging.getLogger('WarBact')
    logger.setLevel(logging.DEBUG)

    # Форматтер
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Обработчик для файла
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(logs_dir, 'game.log'),
        maxBytes=1024*1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Обработчик для консоли
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger