
class stdio:
    @staticmethod
    def output(*args):
        print(*args)


class PackageInfo:
    def __init__(
        self,
        name=None,
        description=None,
        author=None,
        version=None,
    ):
        self.name = name
        self.description = description
        self.author = author
        self.version = version

class Package:
    def __init__(
        self,
        name=None,
        description=None,
        author=None,
        version=None,
    ):
        self.info = PackageInfo(name, description, author, version)
        self.events = {}
    
    def connect(self, event, func):
        if not callable(func):
            raise TypeError("function argument must be callable.")
        self.events[event] = func