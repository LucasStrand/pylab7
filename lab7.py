import socket
import select

port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(1)

listOfSockets = [sockL]

print("Listening on port {}".format(port))
while True:
  tup = select.select(listOfSockets, [], [])
  sock = tup[0][0]

  if sock == sockL:

  #TODO: A new client connects,
  #*call (sockClient, addr) = sockL.accept() and take care of the new client
  #*add the new socket to listOfSockets
  #*notify all other clients aobut the new client
    (sockC, addr) = sockL.accept()
    #?for i in range(1-10):
    listOfSockets.append(sockC)
    sockC.send(bytearray('Connnected', 'ascii'))

    for socket in listOfSockets:
      if(socket != sockL and socket != sockC):
        peername = sockC.getpeername()
        connected = print("{} connected".format(peername))
        socket.send(bytearray(str(connected), 'ascii'))

  else:
    #Connected clients and send data or are disconnected
    data = socket.recv(2048)
    if not data:
      listOfSockets.remove(sock)
      sock.close()
      for socket in listOfSockets:
        if (socket != sockL):
          peername = sockC.getpeername()
          disconnected = print("{} disconnected".format(peername))
          sockC.sendall(bytearray(disconnected, 'ascii'))

    else:
      addrName = "[{}]".format(sock.getpeername())
      for socket in listOfSockets:
        if (socket != sockL):
          message = addrName + data.decode('ascii')
          socket.send(bytearray(message, 'ascii'))
    #TODO: A client sends a message
    #*data is a message from client
    #*send the data to all clients