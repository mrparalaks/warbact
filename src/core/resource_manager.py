import pygame
import os
from typing import Dict
from src.core.logging_setup import logger

class ResourceManager:
    """Менеджер ресурсов игры"""

    def __init__(self) -> None:
        self.textures: Dict[str, pygame.Surface] = {}
        self.fonts: Dict[str, pygame.font.Font] = {}
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.music: Dict[str, pygame.mixer.Sound] = {}
        logger.info("Инициализирован менеджер ресурсов")

    def load_texture(self, name: str, path: str) -> pygame.Surface:
        """Загрузка текстуры"""
        if name in self.textures:
            return self.textures[name]

        try:
            full_path = os.path.join("assets", "textures", path)
            texture = pygame.image.load(full_path).convert_alpha()
            self.textures[name] = texture
            logger.debug(f"Загружена текстура: {name}")
            return texture
        except Exception as e:
            logger.error(f"Ошибка загрузки текстуры {name}: {e}")
            # Создаём пустую поверхность как запасной вариант
            return pygame.Surface((32, 32))

    def get_texture(self, name: str) -> pygame.Surface:
        """Получение текстуры по имени"""
        return self.textures.get(name, pygame.Surface((32, 32)))

    def load_font(self, name: str, path: str, size: int) -> pygame.font.Font:
        """Загрузка шрифта"""
        if name in self.fonts:
            return self.fonts[name]

        try:
            full_path = os.path.join("assets", "fonts", path)
            font = pygame.font.Font(full_path, size)
            self.fonts[name] = font
            logger.debug(f"Загружен шрифт: {name}")
            return font
        except Exception as e:
            logger.error(f"Ошибка загрузки шрифта {name}: {e}")
            # Используем системный шрифт как запасной вариант
            return pygame.font.SysFont("Arial", size)

    def get_font(self, name: str) -> pygame.font.Font:
        """Получение шрифта по имени"""
        return self.fonts.get(name, pygame.font.SysFont("Arial", 12))

    def load_sound(self, name: str, path: str) -> pygame.mixer.Sound:
        """Загрузка звука"""
        if name in self.sounds:
            return self.sounds[name]

        try:
            full_path = os.path.join("assets", "sounds", path)
            sound = pygame.mixer.Sound(full_path)
            self.sounds[name] = sound
            logger.debug(f"Загружен звук: {name}")
            return sound
        except Exception as e:
            logger.error(f"Ошибка загрузки звука {name}: {e}")
            return pygame.mixer.Sound(buffer=bytearray(1))  # Пустой звук

    def get_sound(self, name: str) -> pygame.mixer.Sound:
        """Получение звука по имени"""
        return self.sounds.get(name, pygame.mixer.Sound(buffer=bytearray(1)))

    def load_music(self, name: str, path: str) -> None:
        """Загрузка музыки"""
        if name in self.music:
            return

        try:
            full_path = os.path.join("assets", "music", path)
            pygame.mixer.music.load(full_path)
            self.music[name] = full_path
            logger.debug(f"Загружена музыка: {name}")
        except Exception as e:
            logger.error(f"Ошибка загрузки музыки {name}: {e}")

    def play_music(self, name: str, loops: int = -1) -> None:
        """Воспроизведение музыки"""
        if name in self.music:
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(loops)
            logger.debug(f"Воспроизводится музыка: {name}")
