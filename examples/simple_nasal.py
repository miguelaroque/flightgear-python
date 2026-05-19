#!/usr/bin/python3
"""
Simple Nasal example that reads the elapsed sim time and toggles pause.
"""

from flightgear_python.fg_if import TelnetConnection

"""
Start FlightGear with `--telnet=socket,bi,60,localhost,5500,tcp --allow-nasal-from-sockets`
"""
telnet_conn = TelnetConnection('localhost', 5500)
telnet_conn.connect()

# print() output from Nasal comes back as a string
elapsed = telnet_conn.run_nasal('print(getprop("/sim/time/elapsed-sec"));')
print(f'Elapsed: {elapsed}s')

# fgcommand via Nasal, no output expected
telnet_conn.run_nasal('fgcommand("pause");')
print('Paused')
