from .root import DigitalUnit

class Volume(DigitalUnit):
    def __init__(self) -> None:
        self.type = 'Volume'

class CubicMeter(Volume):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1.0 
        self.measure_add = 0
    def __str__(self) -> str:
        return 'm³'
    
class CubicCentimeter(Volume):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1e-06
        self.measure_add = 0
    def __str__(self) -> str:
        return 'cm³'

class CubicDecimeter(Volume):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 0.001
        self.measure_add = 0.0
    def __str__(self) -> str:
        return 'dm³'
    
class Liter(Volume):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 0.001
        self.measure_add = 0.0
    def __str__(self) -> str:
        return 'L'
    
class MilliLiter(Volume):
    def __init__(self) -> None:
        super().__init__()
        self.measure = 1e-06
        self.measure_add = 0.0
    def __str__(self) -> str:
        return 'mL'
