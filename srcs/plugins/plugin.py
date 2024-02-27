from    abc \
        import  ABC, abstractmethod

class   Plugin(ABC):
    @abstractmethod
    def __init__(self):
        pass