import json
import time
import pycom
from remote import RaspberryPi  # , StartIoT


def main():
    config = json.load(open('config.json'))
    pi: RaspberryPi = RaspberryPi()
    # cloud: StartIoT = StartIoT((config['dev_eui'], config['app_eui'], config['app_key']))

    pycom.rgbled(0x111111)

    while True:

        received: str = pi.receive()
        pycom.rgbled(0x00ff00)
        if received == 'stop':
            break
        time.sleep(0.5)

    pycom.rgbled(0x150000)


if __name__ == '__main__':
    pycom.heartbeat(False)
    pycom.rgbled(0xff0000)
    main()
