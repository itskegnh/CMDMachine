from packager import Package
from packager import stdio

class Mover(Package):
    
    # Package Constructor
    def __init__(self):
        super().__init__(
            name        = "Mover",
            description = "This package introduces the Mover cell into the game.",
            author      = "kegnh",
            version     = "0.0.1"
        )

        self.connect("load", self._load)
    
    def _load(self):
        stdio.output('Thanks for using the Mover Package.')

if __name__ == '__main__':
    Mover()._load()