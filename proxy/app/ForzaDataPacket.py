# -*- coding: utf-8 -*-
from struct import unpack
from ForzaConstants import SLED_FORMAT, DASH_FORMAT
from ForzaConstants import SLED_PROPS, DASH_PROPS


class ForzaDataPacket:
    # This class rappresent a single udp packet sent from the game.
    # Code is inspired by the work of https://github.com/nettrom/forza_motorsport

    def __init__(self, data, packet_type):
        self.packet_type = packet_type

        field_names = self.get_field_names()
        frame_format = self.get_frame_format()
        frame_data = self.get_frame_data(data)

        # dynamically set class attributes from the udp datastream
        for key, value in zip(field_names, unpack(frame_format, frame_data)):
            setattr(self, key, float(value))

    def get_field_names(self):
        # list of field names, in order, based on the packet type.
        # @return: list of strings
        if self.packet_type == 'sled':
            return SLED_PROPS
        elif self.packet_type == 'dash':
            return SLED_PROPS + DASH_PROPS
        elif self.packet_type == 'fh4':
            return SLED_PROPS + DASH_PROPS
        else:
            raise NotImplementedError

    def get_frame_format(self):
        # conversion table for unpacking datastream.
        # @return: string format for struct lib
        if self.packet_type == 'sled':
            return SLED_FORMAT
        return DASH_FORMAT

    def get_frame_data(self, frame_data):
        # exclude unknown data from Forza Horizon packets.
        # @frame_data: datastream from the game
        # @return: readable part of datastream as string, based on packet type
        if self.packet_type == 'fh4':
            return frame_data[:232] + frame_data[244:323]
        return frame_data

    def to_dict(self, filtered_fields=False):
        # dict representation of the class
        # @filtered_fields: subset of fields you want, as list of strings
        # @return: dict
        field_names = self.get_field_names()
        if filtered_fields:
            field_names = [name for name in filtered_fields if name in field_names]
        return {field_name: getattr(self, field_name) for field_name in field_names}
