import socket
from queue import Queue
import threading
from natsort import natsorted, ns

result = []
ziel = "127.0.0.1"

"""
#langsam
def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _ = s.connect((ziel, port))
        return True
    except:
        return False


for x in range(500):
    if (portscan(x)):
        print(f"Port {x} ist offen!")
    else:
        print(f"Port {x} ist geschlossen!")
"""

q = Queue()
for x in range(500):
    q.put(x)


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _ = s.connect((ziel, port))
        return True
    except:
        return False


def worker():
    while q.empty() != True:
        port = q.get()
        if(portscan(port)):
            result.append("Port {} ist offen!".format(port))
        else:
            result.append("Port {} ist geschlossen!".format(port))


# create 50 threads to scan the ports
for x in range(50):
    t = threading.Thread(target=worker)
    t.start()

# warten bis die Threads fertig sind
t.join()
# nach ports sortieren - sort muss manuell gemacht werden - SEARCH for HUMAN NATURAL SORT
result = natsorted(result, alg=ns.IGNORECASE)
print(result)
