# Bluetooth DoS Attack Script

## Overview
This script demonstrates a Denial of Service (DoS) attack on Bluetooth devices. It's designed strictly for educational and testing purposes. Unauthorized use against devices without explicit permission is illegal and punishable by law.

## Disclaimer
This script is for educational purposes only. Any unauthorized use against devices you do not own or without explicit permission is illegal and punishable by law. By using this script, you agree to do so responsibly and at your own risk.

## Source
Repository: [https://github.com/infimiIT/bluetoothDOS](https://github.com/infimiIT/bluetoothDOS)

## Requirements
- Linux system with `hcitool` and `l2ping`
- Python 3.x

## Usage
1. Clone the Repository:
   `git clone https://github.com/yourusername/bluetoothDOS.git`
   `cd bluetoothDOS`

2. Run the Script with Elevated Privileges:
   `sudo python3 do_the_job.py`
   - Follow the prompts to agree to the terms and select the target device for the DoS attack.

## Configuration
Configure the script using command-line arguments:
- `--size`: Packet size in bytes (default: 600)
- `--count`: Number of packets to send (default: 100)
- `--threads`: Number of threads (default: 20)
- `--log`: Log level (default: info)

   Example:
   `sudo python3 do_the_job.py --size 800 --count 200 --threads 30 --log debug`

## License
Provided "as-is" without warranty. Use responsibly and with proper authorization.

## Credits
Project created by Przemysław Myk
GitHub: infimiIT
