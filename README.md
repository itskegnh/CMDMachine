# CMDMachine
CMDMachine is a Cell Machine remake inspired by ModularCM.

## Creating Packages
```py
from packager import Package

class ExamplePackage(Package):
    
    # Package Constructor
    def __init__(self):
        super().__init__(
            name="ExamplePackage",
            description="An example package",
            author="CMDMachine",
            version="1.0.0",
        )

    # Package Functions
    # load: called when a package is loaded by the package manager.
    # unload: called when a package is unloaded by the package manager.
    # tick: called once every tick.
    # update: called every time the game is advanced.
    # key_down: called when a key is pressed.
    # key_up: called when a key is released.
    # mouse_down: called when a mouse button is pressed.
    # mouse_up: called when a mouse button is released.

    # P
