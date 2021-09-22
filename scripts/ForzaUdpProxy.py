#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import socket

from ForzaDataPacket import ForzaDataPacket

TELEGRAF_HOST = 'localhost'
TELEGRAF_PORT = 8094


def dump_stream(source_port, packet_type='fh4', verbose=False):
    # Listens to UDP packets on the given port, convert datastream into
    # human-readable json then send it to a Telegraf instance.
    # @source_port: listening port number (int)
    # @packet_type: packet type sent by the game (string)
    # @verbose: print data to stdout (bool)

    logging.info('listening on port {}'.format(source_port))
    # server_socket = Forza Horizon
    # client_socket = Telegraf instance
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', source_port))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((TELEGRAF_HOST, TELEGRAF_PORT))

    while True:
        # datastream to object
        message, address = server_socket.recvfrom(1024)
        frame = ForzaDataPacket(message, packet_type)

        # object2dict, then add InfluxDB table name
        frame_dict = frame.to_dict()
        frame_dict['measurement'] = 'telemetry'

        if verbose:
            logging.info(frame_dict)
            print(frame_dict)

        # now forward data to Telegraf
        frame_json_str = json.dumps(frame_dict)
        client_socket.sendall(frame_json_str.encode())


def main():
    description = 'Grabs data from a Forza Horizon stream and send to Telegraf.'
    cli_parser = argparse.ArgumentParser(description=description)
    cli_parser.add_argument('port', type=int, help='port number to listen on')
    cli_parser.add_argument('-v', '--verbose', action='store_true', help='also write data to stdout')

    # [TODO] support for FM7 sled/dash is untested
    # cli_parser.add_argument('-t', '--type', type=str, default='fh4',
    #     choices=['sled', 'dash', 'fh4'], help='format of the packets coming from the game'
    # )

    args = cli_parser.parse_args()
    dump_stream(args.port, 'fh4', args.verbose)
    return()


if __name__ == "__main__":
    main()
