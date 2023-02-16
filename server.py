import socket
import threading
import sys


def assign_ranks(client, clients, clients_data):
    """assign ranks to clients on first come first serve basis """
    clients.append(client)
    rank = len(clients) - 1
    client.send("Your rank is {}".format(rank).encode())
    clients_data[client] = rank
    return rank

def distribute_command(clients_data, client_rank, command):
    for socket, rank in clients_data.items():
        # check if the rank of the recipient client is higher than the rank of the sender
        if client_rank < int(rank):
            try:
                # send the command to the recipient client
                new_command = "{} {}".format(command, client_rank)        
                socket.sendall(new_command.encode())
                print(f"Command executed by client with rank {rank}")
                return
            except Exception as e:
                print(f"Error sending command to client with rank {rank}: {e}")
    print("[command rejected]...no client with higher rank found to execute command")

def update_after_disconnect(clients):
    new_dict = {}
    for idx, sock in enumerate(clients):
        new_dict[sock] = idx
       
    return new_dict
    
def handle_client(conn, clients_data, clients):
    global current_clients
    connected = True
    while connected:
        message = conn.recv(1024).decode()
        if not message:
           break

        sender_rank = int(message.split()[1])

        # if message is a command distribute it
        if message.startswith("C"):
            command = message[1:]
            distribute_command(clients_data, sender_rank, command)
        
    print("[Disconnect]  socket {} has disconnected".format(conn.getpeername()))
    conn.close()
    current_clients -= 1
    clients.remove(conn)
    del clients_data[conn]    
    print("[New ranking]")
    clients_data = update_after_disconnect(clients)
    if len(clients) >= 1:
        for sock, rank in clients_data.items():
            print("socket {} has rank number {}".format(sock.getpeername(), rank))
        for i, c in enumerate(clients):
            c.send(f'RYour rank is now {i}'.encode())
    else:
        print("0 connections")        

def start():
    global current_clients
    clients = []
    clients_data = {}

    try:
        max_clients = int(sys.argv[1])
    except IndexError:
        max_clients = 5


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))

    print("[STARTING] Listening for {} clients...".format(max_clients))
    server.listen(max_clients)

    try:
        while True:
            if current_clients >= max_clients:
                continue
            conn, addr = server.accept()
            current_clients += 1
            print("Accepted client {}".format(addr))
            rank = assign_ranks(conn, clients, clients_data)

            client_thread = threading.Thread(target=handle_client, args=(conn, clients_data, clients))
            client_thread.start()
             
            for sock, rank in clients_data.items():
                print("socket {} has rank number {}".format(sock.getpeername(), rank))        

    except (KeyboardInterrupt, ConnectionResetError):
        print('Closing server...')

    finally:
        # Close the socket and unbind the port
        server.close()

current_clients = 0
start()
