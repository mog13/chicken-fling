#!/usr/bin/env python

import thread
import threading
import time
import signal
import sys
import socket
import select



class ThreadServer(threading.Thread):

  SOCKETS = []

  def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter

  def run(self):
    ThreadServer.listen(self.name, 1, self.counter)

  @staticmethod
  def listen(threadName, delay, counter):
    HOST = '0.0.0.0'
    PORT = 10000

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mysock.bind((HOST, PORT))
    mysock.listen(10)
    print 'Starting up on %s port %s' % (HOST, PORT)

    ThreadServer.SOCKETS.append(mysock)

    while True:

      if ChickenFling.running is False:
        mysock.close()
        thread.exit()

      ready_to_read, ready_to_write, in_error = select.select(ThreadServer.SOCKETS, [], [], 1)

      for incomming in ready_to_read:
        if incomming == mysock:
          sockfd, addr = mysock.accept()
          ThreadServer.SOCKETS.append(sockfd)
          print "Client (%s, %s) connected" % addr
        else:
          data = incomming.recv(10)
          if data:
            print "data: " + data
          else:
            # remove the socket that's broken
            if incomming in ThreadServer.SOCKETS:
                ThreadServer.SOCKETS.remove(incomming)
                print "Removed connection"

"""
Simple class for general program variables
"""
class ChickenFling:
  running = True

  @staticmethod
  def signal_int(signal, frame):
    print('Please wait killing threads')
    ChickenFling.running = False

  @staticmethod
  def main():

    signal.signal(signal.SIGINT, ChickenFling.signal_int)

    # Create new threads
    thread1 = ThreadServer(1, "Thread-1", 3)
    thread1.start()
    thread1.join()

    print "Exiting"


ChickenFling.main()
