#!/usr/bin/env python -u

import signal
import select
import logging

from app.Server import Server

"""
Simple class for general program variables
"""
class ChickenFling:

    @staticmethod
    def signal_int(signal, frame):
        logging.info("Shutting Down...")

    @staticmethod
    def main():
        logging.basicConfig(level=logging.DEBUG)
        signal.signal(signal.SIGINT, ChickenFling.signal_int)
        server = Server()
        server.listen()
        logging.info("Exiting!")

if __name__ == '__main__':
    ChickenFling.main()
