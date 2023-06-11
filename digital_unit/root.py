class DigitalUnit:
    def __init__(self) -> None:
        self.type = "NONE"


class Number:
    def __init__(self, number:float, unit:DigitalUnit) -> None:
        self.digital_part = number
        if unit.__class__.__base__.__base__ == DigitalUnit:
            self.unit = unit
        else:
            print(unit.__class__.__base__.__base__)
            raise TypeError('You should set the unit parameter to numerical units.')

    def change_unit(self, new_unit:DigitalUnit) -> None:
        if new_unit.__class__.__base__.__base__ == DigitalUnit:
            if new_unit.type == self.unit.type:
                self.digital_part = self.digital_part * self.unit.measure / new_unit.measure + (new_unit.measure_add-self.unit.measure_add)
                self.unit = new_unit
            else:
                raise TypeError('Different unit types')
        else:
            raise TypeError('You should set the unit parameter to numerical units.')
    
    def __str__(self) -> str:
        return f'{self.digital_part}{self.unit}'
    
    def __abs__():
        return abs(Number)