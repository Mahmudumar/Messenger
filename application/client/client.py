import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init

class Client:
        # init colors
    init()

    # set the available colors
    colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
            Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
            Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
            Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
            ]

    # choose a random color for the client
    client_color = random.choice(colors)
    # server's IP address
    # if the server is not on this machine,
    # put the private (network) IP address (e.g 192.168.1.2)
    SERVER_HOST =socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 5050  # server's port
    separator_token = "<SEP>"  # we will use this to separate the client name & message

    def __init__(self) -> None:
        # initialize TCP socket (for client)
        self.s = socket.socket()
        print(f"[*] Connecting to {self.SERVER_HOST}:{self.SERVER_PORT}...")
        # connect to the server
        self.s.connect((self.SERVER_HOST, self.SERVER_PORT))
        print("[+] Connected.")
        
        # # make a thread that listens for messages to this client & print them
        t = Thread(target=self.listen_for_messages)
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()


    def listen_for_messages(self):
        message = self.s.recv(1024).decode('utf-8')
        #message = decrypt(message, 'key.key')
        # decrypt message
        print("\n" + message)

    def send_messages(self,to_send):
        # add the datetime, name & the color of the sender
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 2
        to_send = f"{self.client_color}[{date_now}] name: {to_send}{Fore.RESET}"
        #session_key_public = generate_key()
        # encrypt the message b4 sending
        #to_send = encrypt(to_send, session_key_public)
        # finally, send the message
        self.s.send(to_send.encode())
