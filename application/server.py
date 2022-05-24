import socket
from threading import Thread
import threading
from datetime import datetime
# server's IP address
SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5050
ADDR = (SERVER_HOST, SERVER_PORT)
separator_token = "<SEP>"

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind(ADDR)
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")


def now():
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date_now


def log(type_, message):
    log = '\n'+f'{type_} >>> [{now()}] ---> {message}'
    print(log)
    return log


def listen_for_client(cs: socket.socket, i=False):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    name = cs.recv(1024).decode()
    log('Connection', f'{cs.getsockname()} just connected as {name}')
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()

        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP>
            # token with ": " for nice printing

            log('Message', f'{name} sent :{msg}')
            # actual message
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())


while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket, client_address))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
    print(f"[ACTIVE CONNECTIONS] - {threading.active_count() - 1}")

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()
