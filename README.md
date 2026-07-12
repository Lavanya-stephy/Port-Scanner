# 🌐 Port Scanner

A Python-based Port Scanner that scans a specified range of ports on a target host or IP address. The application identifies open and closed ports, displays the associated service names, measures the response time for each port, shows a real-time scanning progress bar, and allows users to save the scan results as a report.

## 📌 Features

- ✅ Accepts both **hostname** and **IP address** as input
- ✅ Allows users to specify a custom port range
- ✅ Scans ports using TCP socket connections
- ✅ Detects whether each port is open or closed
- ✅ Displays the common service associated with each port
- ✅ Measures the response time for every scanned port
- ✅ Displays the total time taken for the complete scan
- ✅ Real-time scanning progress using **tqdm**
- ✅ Colored terminal output using **Colorama**
- ✅ Option to save scan results as a report
- ✅ Interactive Command Line Interface (CLI)

## 🛠 Technologies Used

- Python 3
- Socket Programming
- `socket` module
- `time` module
- `tqdm`
- `colorama`

## 📂 Project Structure

```
Port-Scanner/
│
├── __pycache__/              # Python cache files
├── Output/                   # Saved scan reports
├── color.py                  # Terminal color configuration
├── Main_Port_Scanner.py      # Main application entry point
├── report.py                 # Handles report generation and saving
├── Scanner.py                # Core port scanning functionality
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Port-Scanner
```

Install the required libraries:

```bash
pip install tqdm colorama
```

Run the application:

```bash
python Main_Port_Scanner.py
```

## 💻 Sample Output

```text
Enter Host name or IP address: google.com
Enter your range (separated by ,): 80,90

Scanning in progress...

Total time taken: 10.18s

PORT      STATUS             SERVICE       TIME
80        Open               http          0.015s
81        Closed/Filtered    hosts2-ns     1.005s
82        Closed/Filtered    Unknown       1.007s
...
90        Closed/Filtered    Unknown       1.009s

Do you want to save the report? (yes/no): yes

REPORT SAVED SUCCESSFULLY
```

## 📚 Python Concepts Used

- Socket Programming
- Exception Handling
- Functions
- Loops
- File Handling
- Progress Bars (`tqdm`)
- Terminal Styling (`Colorama`)
- Timing Functions
- Networking Fundamentals

## ⚠ Disclaimer

This project is intended **for educational purposes only**.

Only scan systems and networks that you own or have explicit permission to test. Unauthorized port scanning may violate laws or organizational policies.

## 📈 Learning Outcomes

This project helped me understand:

- TCP/IP Networking
- Port Scanning Techniques
- Socket Programming in Python
- Service Identification
- Measuring Network Response Time
- Building Interactive Command-Line Applications
- Creating Professional Terminal Interfaces

## 📜 License

This project is developed for educational purposes.