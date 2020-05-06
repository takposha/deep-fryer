import os
import re
import tempfile
import random
import subprocess
import ffmpy
import json

def get_dimensions(input_file):
    """
    Parse a video's resolution (1024x720) and return width + height
    """
    deets = get_video_details(input_file)
    dimensions = deets['width'],deets['height']
    width = int(dimensions[0])
    height = int(dimensions[1])
    return width, height


def get_total_seconds(input_file):
    """
    Parse a video's duration (00:00:00) and convert to total seconds
    """
    deets = get_video_details(input_file)
    
    duration = deets['duration']
    print(duration)

    return float(duration)


def make_random_value(val_range):
    """
    Turn an array of 2 value ranges into float rounded to 2 decimal places
    eg [2, 3] => 2.33
    """
    return round(random.uniform(*val_range), 2)


def line_break(num):
    for _ in range(num):
        print('')


def get_video_details(input_file):
    
    tup_resp = ffmpy.FFprobe(
    inputs={input_file: None},
    global_options=[
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format', '-show_streams']
    ).run(stdout=subprocess.PIPE)

    meta = json.loads(tup_resp[0].decode('utf-8'))
    
    return meta['streams'][0]
