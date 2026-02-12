from pathlib import Path
from pygame import mixer

from game.settings import GameSettings

class SoundManager: 
    def __init__(self):
        self.sounds_dir: Path = GameSettings.SOUNDS_DIR
        self.music_dir: Path = GameSettings.MUSIC_DIR
    
    def _load(self, file_name: str) -> None:
        """
        Carga una pista de sonido de forma generica
        
        Args:
            file_name(str): Nombre del archivo de sonido.
        """
        return mixer.music.load(filename=file_name)
    
    def play_effect(self, effect_name: str) -> None:
        """
        Reproduce un efecto de sonido.
        
        Args:
            effect_name (str): Nombre del archivo del efecto de sonido.
        """
        filename = self.sounds_dir / f"{effect_name}"
        return self._load(str(filename))
    
    def play_music(self, track_name: str) ->  None:
        """
        Reproduce un una pista de musica del juego.
        
        Args:
            track_name (str): Nombre del archivo de la pista.
        """
        filename = self.music_dir / f"{track_name}"
        return self._load(str(filename))
    
    def stop_all_sounds(self) -> None:
        """
        Detiene todos los sonidos que se esten ejecutando.
        """
        return mixer.music.stop()