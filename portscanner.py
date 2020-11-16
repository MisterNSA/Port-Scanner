import socket
from queue import Queue
import threading
from natsort import natsorted, ns

result = []
dest = "127.0.0.1"

"""
#langsam
def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _ = s.connect((dest, port))
        return True
    except:
        return False


for x in range(500):
    if (portscan(x)):
        print(f"Port {x} is open!")
    else:
        print(f"Port {x} ist closed!")
"""

q = Queue()
for x in range(500):
    q.put(x)


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _ = s.connect((dest, port))
        return True
    except:
        return False


def worker():
    while q.empty() != True:
        port = q.get()
        if(portscan(port)):
            result.append("Port {} is open!".format(port))
        else:
            result.append("Port {} ist closed!".format(port))


# create 50 threads to scan the ports
for x in range(50):
    t = threading.Thread(target=worker)
    t.start()

# wait til all threads are done
t.join()

# Without this awesome natsort library, the ports wouldend be in order
result = natsorted(result, alg=ns.IGNORECASE)
print(result)
