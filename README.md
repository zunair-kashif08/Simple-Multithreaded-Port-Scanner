# Simple-Multithreaded-Port-Scanner

A multithreaded TCP port scanner implemented in Python, designed to demonstrate core concepts in network programming, concurrency, and basic cybersecurity analysis.

---

## Overview

The Simple Multithreaded Port Scanner efficiently scans a range of TCP ports on a target system by leveraging multiple threads. This significantly reduces scan time compared to sequential scanning.

This project also includes demonstration media and a report illustrating how port scanning interacts with firewall rules and detection mechanisms.

---

## Features

* Multithreaded port scanning for improved performance
* Custom target IP and port range input
* Thread-safe implementation using mutex locks
* Clear display of open ports
* Includes demonstration videos of firewall behavior
* Includes detailed project report

---

## How It Works

1. The user inputs:

   * Target IP address
   * Start port
   * End port

2. The port range is divided among multiple threads

3. Each thread:

   * Attempts to connect using TCP sockets
   * Uses `socket.connect_ex()` to determine port status

4. Open ports are stored in a shared list

5. A mutex lock (`threading.Lock`) ensures safe access to shared data

6. Final results are sorted and displayed

---

## Technical Details

| Component       | Description               |
| --------------- | ------------------------- |
| Language        | Python 3                  |
| Protocol        | TCP                       |
| Libraries       | socket, threading         |
| Concurrency     | Multithreading            |
| Synchronization | Mutex Lock                |
| Timeout         | Approximately 0.5 seconds |
| Threads         | Approximately 10          |

---

## Project Structure

```text
Simple-Multithreaded-Port-Scanner/
│
├── port_scanner.py
├── Project.pdf
├── Before Firewall Rule.mp4
├── After Firewall Rule.mp4
└── README.md
```

---

## Requirements

* Python 3.x
* No external dependencies required

---

## Installation

Clone the repository:

```bash
git clone https://github.com/zunair-kashif08/Simple-Multithreaded-Port-Scanner.git
cd Simple-Multithreaded-Port-Scanner
```

---

## Usage

Run the scanner:

```bash
python port_scanner.py
```

### Example Input

```
Enter the target IP address: 192.168.1.1
Enter the start port: 1
Enter the end port: 1000
```

### Example Output

```
Open Ports are:
[22, 80, 443]
```

---

## Concurrency and Synchronization

This project demonstrates safe handling of shared resources in a multithreaded environment.

* Multiple threads scan ports concurrently
* A shared list stores open ports
* A mutex lock ensures only one thread modifies shared data at a time

This prevents race conditions and ensures consistent results.

---

## Security Context

This project relates to foundational cybersecurity concepts:

* Port scanning techniques
* Firewall rule behavior
* Logging and detection of scanning activity

Included materials demonstrate:

* Scanning behavior before firewall rules
* Scanning behavior after firewall rules
* Detection and logging mechanisms

---

## Disclaimer

This tool is intended for educational purposes only.

Do not scan systems without permission. Unauthorized scanning may be illegal.

---

## Limitations

* TCP scanning only
* Fixed thread count
* No service detection
* Limited input validation
* No export functionality

---

## Future Improvements

* Configurable thread count
* UDP scanning support
* Banner grabbing
* Command-line argument support
* Export results (CSV, JSON)
* GUI interface
* Progress indicators and timing metrics

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## License

This project is open-source. Consider adding a license such as MIT.

---

## Author

Developed as part of an academic project in networking, operating systems, and cybersecurity.

GitHub: https://github.com/zunair-kashif08
