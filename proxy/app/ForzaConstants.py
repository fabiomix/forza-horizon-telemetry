# -*- coding: utf-8 -*-

# Format string that allows unpack of data bytestream
# for the V1 format called 'sled'
SLED_FORMAT = '<iIfffffffffffffffffffffffffffffffffffffffffffffffffffiiiii'

# Format string that allows unpack of data bytestream
# for the V2 format called 'dash'
DASH_FORMAT = '<iIfffffffffffffffffffffffffffffffffffffffffffffffffffiiiiifffffffffffffffffHBBBBBBbbb'

# Names of the properties in the order they're featured in the 'sled' packet:
SLED_PROPS = [
    'is_race_on', 'timestamp_ms',
    'engine_max_rpm', 'engine_idle_rpm', 'current_engine_rpm',
    'acceleration_x', 'acceleration_y', 'acceleration_z',
    'velocity_x', 'velocity_y', 'velocity_z',
    'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z',
    'yaw', 'pitch', 'roll',
    'norm_suspension_travel_FL', 'norm_suspension_travel_FR',
    'norm_suspension_travel_RL', 'norm_suspension_travel_RR',
    'tire_slip_ratio_FL', 'tire_slip_ratio_FR',
    'tire_slip_ratio_RL', 'tire_slip_ratio_RR',
    'wheel_rotation_speed_FL', 'wheel_rotation_speed_FR',
    'wheel_rotation_speed_RL', 'wheel_rotation_speed_RR',
    'wheel_on_rumble_strip_FL', 'wheel_on_rumble_strip_FR',
    'wheel_on_rumble_strip_RL', 'wheel_on_rumble_strip_RR',
    'wheel_in_puddle_FL', 'wheel_in_puddle_FR',
    'wheel_in_puddle_RL', 'wheel_in_puddle_RR',
    'surface_rumble_FL', 'surface_rumble_FR',
    'surface_rumble_RL', 'surface_rumble_RR',
    'tire_slip_angle_FL', 'tire_slip_angle_FR',
    'tire_slip_angle_RL', 'tire_slip_angle_RR',
    'tire_combined_slip_FL', 'tire_combined_slip_FR',
    'tire_combined_slip_RL', 'tire_combined_slip_RR',
    'suspension_travel_meters_FL', 'suspension_travel_meters_FR',
    'suspension_travel_meters_RL', 'suspension_travel_meters_RR',
    'car_ordinal', 'car_class', 'car_performance_index',
    'drivetrain_type', 'num_cylinders'
]

# The additional props added in the 'dash' format
DASH_PROPS = [
    'position_x', 'position_y', 'position_z',
    'speed', 'power', 'torque',
    'tire_temp_FL', 'tire_temp_FR',
    'tire_temp_RL', 'tire_temp_RR',
    'boost', 'fuel', 'dist_traveled',
    'best_lap_time', 'last_lap_time',
    'cur_lap_time', 'cur_race_time',
    'lap_no', 'race_pos',
    'accel', 'brake', 'clutch', 'handbrake',
    'gear', 'steer',
    'norm_driving_line', 'norm_ai_brake_diff'
]
