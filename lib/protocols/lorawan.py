import time
import socket
from network import LoRa
from typing import Tuple
from protocols import Protocol


class LoRaWAN(Protocol):
    def __init__(self, mode=LoRa.LORAWAN):
        super().__init__()
        self.socket = None
        self.lora = LoRa(mode=mode)

    def connect(self, auth: Tuple, timeout=0, activation=LoRa.OTAA, retry_function=None, blocking=False):
        self.lora.connect(activation=activation, auth=auth, timeout=timeout)

        if timeout == 0:
            while not self.lora.has_joined():
                if retry_function:
                    retry_function()
                else:
                    time.sleep(1)
        else:
            for x in range(timeout):
                if self.lora.has_joined():
                    break
                if retry_function:
                    retry_function()
                else:
                    time.sleep(1)

        if not self.lora.has_joined():
            return False

        self.socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

        # set the LoRaWAN data rate
        self.socket.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

        # make the socket non-blocking
        self.socket.setblocking(blocking)

        return True

    def send(self, data: str):
        self.socket.send(data)

    def receive(self, length: int):
        return self.socket.receive(length)
