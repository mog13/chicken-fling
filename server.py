#!/usr/bin/env python -u

import signal
import select

from app.Server import Server

"""
Simple class for general program variables
"""
class ChickenFling:

    @staticmethod
    def signal_int(signal, frame):
        print "\nShutting Down...",

    @staticmethod
    def main():
        signal.signal(signal.SIGINT, ChickenFling.signal_int)
        server = Server()
        server.listen()
        print "Exiting!"

if __name__ == '__main__':
    ChickenFling.main()
