# Этот файл делает папку src Python-пакетом
from .core.logging_setup import setup_logging
from .core.state import State

# Объявляем, что доступно при импорте пакета src
__all__ = ['setup_logging', 'State']
