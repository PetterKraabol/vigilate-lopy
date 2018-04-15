import time
from machine import UART


class RaspberryPi:
    def __init__(self, baud_rate: int = 115200):
        self.uart: UART = UART(1, baud_rate, bits=8, parity=None, stop=1)
        self.uart.init(baudrate=baud_rate, bits=8, parity=None, stop=1)

    def receive(self, interval: int = 1, attempts: int = -1) -> str:
        while attempts != 0:
            if self.uart.any():
                data = self.uart.read().decode('utf-8')
                return data
            time.sleep(interval)
            attempts = max(attempts - 1, -1)

    def send(self, data: bytes):
        self.uart.write(data)
