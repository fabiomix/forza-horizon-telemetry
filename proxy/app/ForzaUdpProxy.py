#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import json
import socket

from ForzaDataPacket import ForzaDataPacket


def dump_stream(bind_port, packet_type, telegraf_host, telegraf_port, verbose=False):
    """
    Listens to UDP packets on the given port, convert datastream into
    human-readable json then send it to a Telegraf instance.
    @bind_port: port this script listens on (int)
    @packet_type: format of the packets coming from the game (string)
    @telegraf_host: hostname of the Telegraf instance (string)
    @telegraf_port: port of the Telegraf instance (int)
    @verbose: print incoming data to stdout (bool)
    """

    print(f"starting ForzaUdpProxy, listening on port {bind_port}")
    print(f"expected incoming format from the game is: {packet_type}")
    print(f"sending data to Telegraf instance at host {telegraf_host}, port {telegraf_port}")
    print(f"verbose mode is: {bool(verbose)}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', bind_port))

    destination_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destination_socket.connect((telegraf_host, telegraf_port))

    while True:
        # datastream to object
        message, address = server_socket.recvfrom(1024)
        frame = ForzaDataPacket(message, packet_type)

        # object2dict, then add InfluxDB table name
        frame_dict = frame.to_dict()
        frame_dict['measurement'] = 'telemetry'

        if verbose:
            print(frame_dict)

        # now forward data to Telegraf
        frame_json_str = json.dumps(frame_dict)
        destination_socket.sendall(frame_json_str.encode())
    return


def main():
    description = 'Grabs data sent from a Forza Horizon game and forward them to Telegraf in json format.'
    cli_parser = argparse.ArgumentParser(description=description)

    cli_parser.add_argument(
        '-p', type=int, dest='bind_port', default=9999,
        help='port this script listens on (default 9999)')
    cli_parser.add_argument(
        '-f', type=str, dest='format', choices=['sled', 'dash', 'fh4'], default='fh4',
        help='format of the packets coming from the game')
    cli_parser.add_argument(
        '-th', type=str, dest='telegraf_host', default='telegraf',
        help='hostname of the Telegraf instance')
    cli_parser.add_argument(
        '-tp', type=int, dest='telegraf_port', default=8094,
        help='port of the Telegraf instance')
    cli_parser.add_argument(
        '--verbose', action='store_true',
        help='print incoming data to stdout')

    args = cli_parser.parse_args()
    # [TODO] support for FM7 sled/dash is untested
    dump_stream(args.bind_port, 'fh4', args.telegraf_host, args.telegraf_port, args.verbose)
    return


if __name__ == "__main__":
    main()
