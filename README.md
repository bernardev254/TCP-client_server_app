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

## Getting_started

### installing and running the project
on your local terminal:
1. clone the project
```shell
$ git clone

```
2. navigate to the project directory
```
$ cd project directory
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
Listening for 10 clients...
Accepted client ('127.0.0.1', 43664)
socket ('127.0.0.1', 43664) has rank number 0
Accepted client ('127.0.0.1', 48324)
socket ('127.0.0.1', 43664) has rank number 0
socket ('127.0.0.1', 48324) has rank number 1
Accepted client ('127.0.0.1', 54390)
socket ('127.0.0.1', 43664) has rank number 0
socket ('127.0.0.1', 48324) has rank number 1
socket ('127.0.0.1', 54390) has rank number 2
```

5. run the client(s)
open a new terminal window and run  a new client there
```
python3 client.py

```
output
``` client.py
Assigned rank: 0
Enter command: hello world
```


