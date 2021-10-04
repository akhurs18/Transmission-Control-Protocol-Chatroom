# Transmission-Control-Protocol-Chatroom


A Python chatroom application with Tkinter GUI

How to Run?
Run the server.py script from the command line.

Usage: python3 server.py 

Arguments:

host: Interface the server listens at. Can be a hostname, or an IP address.
-p PORT: TCP port the server listens at (default 1060)
For example:

$ python3 server.py 127.0.0.1
Listening at ('127.0.0.1', 1060)
$ python3 server.py localhost
Listening at ('127.0.0.1', 1060)
Run the client.py script from the command line (in a separate terminal window).

Usage: python3 client.py <host> [-p PORT]

Arguments:

host: Interface the server listens at. Can be a hostname, or an IP address.
-p PORT: TCP port the server listens at (default 1060)


Your name:
Run multiple clients to chat in real-time!

Note: If connecting from a different subnet, your firewall may block the connection.
