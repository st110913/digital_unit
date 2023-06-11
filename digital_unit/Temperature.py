from .root import DigitalUnit
class Temperature(DigitalUnit):
    def __init__(self) -> None:
        self.type = 'Temperature'

class CelsiusDegree(Temperature):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1.8 
        self.measure_add = 0.0
    def __str__(self) -> str:
        return '℃'
    
class FahrenheitTegree(Temperature):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1.0 
        self.measure_add = 32.0
    def __str__(self) -> str:
        return '℉'
    
