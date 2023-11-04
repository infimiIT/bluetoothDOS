# Bluetooth DoS Attack Script

This script is a demonstration of a Denial of Service (DoS) attack on Bluetooth devices. It's intended strictly for educational and testing purposes. Unauthorized use against devices without explicit permission is illegal and punishable by law.

## Disclaimer

This script is provided for educational purposes only. Unauthorized use of this script against devices you do not own or have explicit permission to test is illegal and punishable by law. By using this script, you agree to use it for educational purposes only and at your own risk.

## Source

This script is based on the repository: [https://github.com/infimiIT/bluetoothDOS](https://github.com/infimiIT/bluetoothDOS)

## Requirements

- A Linux system with `hcitool` and `l2ping` installed.
- Python 3.x

## Usage

1. Clone this repository:

git clone https://github.com/yourusername/bluetoothDOS.git
cd bluetoothDOS

Run the script with necessary privileges:

sudo python3 do_the_job.py

    When prompted, agree to the terms by typing yes.
    The script will scan and list available Bluetooth devices.
    Enter the number corresponding to the device you want to attack.
    The script will start the DoS attack on the selected device.

##Configuration

You can configure the script using command line arguments:

    --size: Packet size in bytes (default: 600)
    --count: Number of packets to send (default: 100)
    --threads: Number of threads (default: 20)
    --log: Log level (default: info)

Example:

sudo python3 do_the_job.py --size 800 --count 200 --threads 30 --log debug

License

This script is provided "as-is" without any warranty. Use at your own risk, and always obtain proper authorization before conducting penetration tests or security assessments.
