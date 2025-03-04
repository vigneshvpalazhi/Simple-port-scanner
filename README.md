# Simple Port Scanner




A basic Python port scanner that checks for open TCP ports on a specified host.

## Features
- Scans a target host for open TCP ports
- Supports scanning specific port ranges or full port scan (0-65535)
- Displays service names for known ports when available
- Shows scan duration
- Uses socket timeout for faster scanning

## Requirements
- Python 3.x
- No external dependencies required

## Usage
```bash
python port_scanner.py
```
1.Run the script
2.Enter the target host (e.g., "example.com" or IP address)
3.Enter the maximum port number to scan or "full" for complete port scan (0-65535)


### Limitations
* Basic TCP connect scan only
* May be blocked by firewalls
* Scanning all ports (0-65535) can take significant time
* Requires appropriate permissions to run


![Screenshot from 2025-03-04 22-19-22](https://github.com/user-attachments/assets/b99db95a-ab34-426a-a8d4-6a5f77b28c68)
