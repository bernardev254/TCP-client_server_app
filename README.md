# Client-Server Application
## Table of contents

- [overview](#overview)
- [System_Requirements](#system_requirements)
- [Features](#features)
- [Getting_Started](#getting_Started)
- [Known_issues](#known_issues)
- [Author](#author)

## overview
This application allows client to connect to a TCP server, send commands to the server and then the server distributes the commands to lower rank clients for execution

## System_Requirements
- python3
- threading

## Features
### server
- accepts client
- accepts clients commands if a client is not rhe lowest in rank
- distributes commands to lower rank clients
- handles disconnection of clients and re-adjusts

### client
- connects to the server
- send commands to the server
- excecutes commands from the server

### implementation
This project implements a server that exposes a tcp socket where clients can connect and send data.clients can send commands without blocking each other my using python multithreding to achieve concurrency and handle each client on separate thread.

## Getting_started

### installing and running the project
on your local terminal:
1. clone the project
```shell
$ git clone git@github.com:Bkaraba/TCP-client_server_app.git

```
2. navigate to the project directory
```
$ cd TCP-client_server_app
```

3. - install [python3](https://docs.python.org/3/using/unix.html?highlight=install%20python3)
   - install required packages: sockets and threading

```
pip install sockets
pip install threading

```
4. run the server
run the server that accepts 10 connections
```
$ python3 server.py 10

```
output
```server.py
[STARTING] Listening for 10 clients...
Accepted client ('127.0.0.1', 47036)
socket ('127.0.0.1', 47036) has rank number 0
Accepted client ('127.0.0.1', 49910)
socket ('127.0.0.1', 47036) has rank number 0
socket ('127.0.0.1', 49910) has rank number 1
Accepted client ('127.0.0.1', 54500)
socket ('127.0.0.1', 47036) has rank number 0
socket ('127.0.0.1', 49910) has rank number 1
socket ('127.0.0.1', 54500) has rank number 2
Accepted client ('127.0.0.1', 34630)
socket ('127.0.0.1', 47036) has rank number 0
socket ('127.0.0.1', 49910) has rank number 1
socket ('127.0.0.1', 54500) has rank number 2
socket ('127.0.0.1', 34630) has rank number 3
Accepted client ('127.0.0.1', 34640)
socket ('127.0.0.1', 47036) has rank number 0
socket ('127.0.0.1', 49910) has rank number 1
socket ('127.0.0.1', 54500) has rank number 2
socket ('127.0.0.1', 34630) has rank number 3
socket ('127.0.0.1', 34640) has rank number 4
```

5. run the client(s)
open a new terminal window and run  a new client there
```
python3 client.py

```
output
``` client.py
Assigned rank: 0
Enter command: print
```
``` client.py
Assigned rank: 1
Enter command: 
[Processing]......
[Received] received command print from server:
[Executing] i am printing watch me print

Enter command: 
debug 
Enter command: 
```
``` client.py
Assigned rank: 2
Enter command: 
[Processing]......
[Received] received command debug from server:
[Executing] i am debuging watch me debug

Enter command: 
```
on disconnecting

```
[Disconnect]  socket ('127.0.0.1', 41378) has disconnected
[New ranking]
socket ('127.0.0.1', 33300) has rank number 0
socket ('127.0.0.1', 33316) has rank number 1
[Disconnect]  socket ('127.0.0.1', 33316) has disconnected
[New ranking]
socket ('127.0.0.1', 33300) has rank number 0
[Disconnect]  socket ('127.0.0.1', 33300) has disconnected
[New ranking]
0 connections
```

## Known_issues

- The server sends the command for execution to the immediate lower ranked client.I will be implementing a way to distribute commands to clients with lower load in the next iteration 
- 

## Author

- Bernard Karaba
- bkaraba14@gmail.com
- [portfolio](bkaraba.github.io/portfolio)

