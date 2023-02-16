import socket
import threading

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def receive_data(client_socket):
    data = client_socket.recv(1024).decode()
    return data
    

def send_command(client_socket, command):
    client_socket.sendall(command.encode())

def process_command_from_server(command):
    command = command[2:-2]
    print("[Received] received command{} from server:".format(command))
    print("[Executing] i am{}ing watch me{}".format(command, command))
        

def receive_and_execute_command(client_socket):
    
    data = receive_data(client_socket)
    rank = int(data.split()[-1])    

    if data.startswith("R"):
        updated_rank = int(data.split()[-1])
        if (updated_rank != rank):
            print("\nMy new rank is {}".format(updated_rank))
            print("\nEnter command: ")
            rank = updated_rank

    elif int(data.split()[0]) > rank:
        print("\nRejected: Cannot execute command from higher rank client")
        print("\nEnter command: ")

    else:
        # process the received command
        print("\n[Processing]......")
        process_command_from_server(data)
        print("\nEnter command: ")
def listen_for_commands(sock):
    while True:
        receive_and_execute_command(sock)
        

def prompt_for_command(client_socket):
    command = input("Enter command: ")
    send_command(client_socket, "C {} {}".format(rank, command))

if __name__ == '__main__':
    host = 'localhost' # server address
    port = 5555 # server port
    
    client_socket = connect_to_server(host, port)
    rank = int(client_socket.recv(1024).decode().split()[-1])
    print("Assigned rank: {}".format(rank))


    # start the listen_for_commands thread
    listen_thread = threading.Thread(target=listen_for_commands, args=(client_socket,))
    listen_thread.start() 

    # main loop for user input
    prompt = True
    while prompt:
        prompt_for_command(client_socket)
      
        
