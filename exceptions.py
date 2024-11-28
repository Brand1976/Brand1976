"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(TypeError):
    pass


class NotEnoughFuel(LowFuelError):
    pass


class CargoOverload(Exception):
    pass
