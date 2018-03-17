import json
from remote import StartIoT


def main(config: dict):
    server: StartIoT = StartIoT(
        auth=(config['start_iot']['dev_eui'], config['start_iot']['app_eui'], config['start_iot']['app_key']))

    print(server)


if __name__ == '__main__':
    config_dictionary: dict = json.load(open('config.json'))
    main(config_dictionary)
