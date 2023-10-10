# SysAdmin Windows Event Monitoring System

This project is a system event monitoring system for Windows systems. It allows real-time collection of events from the Windows event log and their storage in a CSV file for further analysis.

## Requirements

- Windows RPC (Remote Procedure Call) server available, necessary to obtain events from the Windows event log.
- Python 3.x
- Python Libraries: `pywin32` (for get Windows event log).

You can install the necessary Python libraries using `pip`:

```shell
pip install pywin32
```

## How to use
1. Execute of main script:
   
```python
python engine/main.py
```