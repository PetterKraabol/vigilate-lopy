from protocols import UART
from remote import Component


class RaspberryPi(Component):
    def __init__(self, name='Raspberry Pi'):
        super().__init__(name)
        self.uart: UART = UART()
