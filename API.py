import sys
import re
import socket

    """
    Script to check LOT-Nr and return message of 'hiag_watchdog_win'
    """
    101
if len(sys.argv) < 1:
    print("Missing argument")
    exit()

room = re.sub("LOT\d{4}", "", sys.argv[1])


try:
    roomint = int(room)
except ValueError:
    print("Illegal LOT-Nr: "+sys.argv[1])
    exit()

if roomint < 0 or roomint > 15:
    print("Illegal grow room Nr.")
    exit()

def send_message():
    """
    Script to send messages to the listening server in 'hiag_watchdog_win'.
    """
    s = socket.socket()
    s.connect((IP, port))
    z = room
    s.sendall(z.encode())
    s.close()

# IP of win machine on subnet
IP = '192.168.254.145'
port = 3125

send_message

print("grow room: "+room )
