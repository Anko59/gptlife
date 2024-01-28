class Action:
    def __init__(self, name: str, perform: callable) -> None:
        self.name = name
        self.perform = perform

class ActionError(Exception):
    pass
