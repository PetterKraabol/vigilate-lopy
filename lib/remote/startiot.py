import binascii
from typing import Tuple
from remote import Component
from protocols import LoRaWAN


class StartIoT(Component):
    def __init__(self, auth: Tuple[str, str, str], name='StartIoT'):
        super().__init__(name)
        self.LoRaWAN: LoRaWAN = LoRaWAN()
        self.dev_eui: bytes = None
        self.app_eui: bytes = None
        self.app_key: bytes = None
        self.set_auth(auth)

    def connect(self, blocking=False, timeout=0) -> bool:
        return self.LoRaWAN.connect(auth=(self.dev_eui, self.app_eui, self.app_key), timeout=timeout, blocking=blocking)

    def set_auth(self, auth: Tuple[str, str, str]):
        self.dev_eui: bytes = binascii.unhexlify(auth[0])
        self.app_eui: bytes = binascii.unhexlify(auth[1])
        self.app_key: bytes = binascii.unhexlify(auth[2])

    def send(self, data):
        self.LoRaWAN.send(data)

    def receive(self, length: int):
        return self.LoRaWAN.receive(length)