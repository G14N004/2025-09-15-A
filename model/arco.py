from dataclasses import dataclass

from model.pilota import Pilota


@dataclass
class Arco:
    pilota1:Pilota
    pilota2:Pilota
    peso:int
