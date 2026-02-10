from pygame import display, Surface, image
from pathlib import Path
from typing import List

__version__ = "0.0.0"

class GameSettings:
    # Pantalla
    SCREEN_HEIGHT: int = 600
    SCREEN_WIDTH: int = 1100
    SCREEM_TITLE = "GabsGame-Dino"
    SCREEN: tuple = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Rutas
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    ASSETS_DIR: Path = BASE_DIR / "assets"
    GABSGAME_ASSETS: Path = ASSETS_DIR / "dino"
    PTERODACTIL_ASSTES: Path = ASSETS_DIR / "birds"
    CACTUS_ASSETS: Path = ASSETS_DIR / "cactus"
    OTHER_ASSETS: Path = ASSETS_DIR / "other"

    # ASSETS
    RUNNING: List[Surface] = [
        image.load(GABSGAME_ASSETS / "DinoRun1.png"), 
        image.load(GABSGAME_ASSETS / "DinoRun2.png")
    ]
    CLOUD: Surface = image.load(OTHER_ASSETS / "Cloud.png")
    BG: Surface = image.load(OTHER_ASSETS / "Track.png")

    JUMPING: Surface = image.load(GABSGAME_ASSETS / "DinoJump.png")
    DEAD: Surface = image.load(GABSGAME_ASSETS / "DinoDead.png")
    DUCKING: List[Surface] = [
        image.load(GABSGAME_ASSETS / "DinoDuck1.png"), 
        image.load(GABSGAME_ASSETS / "DinoDuck2.png")
    ]

    SMALL_CACTUS: List[Surface] = [
        image.load(CACTUS_ASSETS / "SmallCactus1.png"), 
        image.load(CACTUS_ASSETS / "SmallCactus2.png"),
        image.load(CACTUS_ASSETS / "SmallCactus3.png")
    ]
    LARGE_CACTUS: List[Surface] = [
        image.load(CACTUS_ASSETS / "LargeCactus1.png"), 
        image.load(CACTUS_ASSETS / "LargeCactus2.png"),
        image.load(CACTUS_ASSETS / "LargeCactus3.png")
    ]
    PTERODACTIL: List[Surface] = [
        image.load(PTERODACTIL_ASSTES / "Bird1.png"), 
        image.load(PTERODACTIL_ASSTES / "Bird2.png")
    ]
    JUMPING_CACTUS: List[Surface] = [
        image.load(CACTUS_ASSETS / "SmallCactus1.png"), 
        image.load(CACTUS_ASSETS / "SmallCactus2.png"),
        image.load(CACTUS_ASSETS / "SmallCactus3.png")
    ]