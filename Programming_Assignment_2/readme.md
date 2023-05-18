
first  run the server using the below command in a terminal window

## python3 server.py

Second run the client using the below command using another terminal window

## python3 client.py

All the scenarios are programmed in the client.py so the ouput would be printed on the console.

For seeing the Timeout Message of "Error - Server does not respond"
Stop the server.py (Ctrl+c on the terminal)

Start the client.py, you would observe that the client makes 3 attempts to contact server and after 3 failed attempts the error message is displayed.



Code Structue

`packets.py` == all the UDP packets are defined in this python file as classes.

`client.py` == UDP client that uses these packets and sends request to the server

`server.py` == UDP server that uses listens to requests with these packets and sends responds to the clients using these packets


