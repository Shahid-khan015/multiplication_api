from flask import Flask, jsonify, send_file, json, send_from_directory , Response 
import pandas as pd
import cv2
import base64
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
import numpy as np
import imageio
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

application = app





# @app.route("/vd")
# def add_api():

    # num_folder = r"website\DataSet\numbers"
    # numbers_links = {}
    # 
    # for nl in os.listdir(num_folder):
        # if nl.isdigit():
            # number = int(nl)
            # numbers_links[number] = rf"{num_folder}/{nl}"
    # 
    # op_folder = r"website\DataSet\operators"
    # operator_links = {}
    # 
    # for opl in os.listdir(op_folder):
        # operator_links[opl] = rf"{op_folder}/{opl}"

#     num1 = 2
#     num2 = 5
#     mul = num1 * num2
#     output_path = rf"website\DataSet\Output\x\{num1}x{num2}={mul}.mp4"
#     toBe_merge = {num1: numbers_links[num1], 'x':  operator_links['x'],
#                   num2: numbers_links[num2], mul:  numbers_links[mul]}

#     video_extensions = ('.mp4', '.avi', '.mov', '.mkv')

#     def video_return(video_path):
#         try:
#             reader = imageio.get_reader(video_path)
#         except Exception as e:
#             return jsonify({"error": f"Could not open video: {str(e)}"})
#         frames_list = []
#         for frame in reader:
#             frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#             frame = cv2.resize(frame, (64, 64))

#             _, buffer = cv2.imencode('.png', frame)
#             encoded_image = base64.b64encode(buffer).decode('utf-8')

#             frames_list.append(encoded_image)
#         # return jsonify({"data": frames_list})


#     def merge_videos(video_path, output_path):
#         clip = [VideoFileClip(video_path) for video_path in video_path.values()]
#         merged_clip = concatenate_videoclips(clip)
#         merged_clip = merged_clip.resize(1)
#         merged_clip.write_videofile(output_path, codec='libx264')


#         # for frame in merged_clip.iter_frames(fps=60, dtype='uint8'):
#         #     yield frame
#     video_files = {}
#     for folder in toBe_merge:
#         if os.path.isdir(toBe_merge[folder]):
#             files = [f for f in os.listdir(toBe_merge[folder]) if f.endswith(video_extensions)]
#             full_paths = [os.path.join(toBe_merge[folder], f) for f in files]
#             for paths in full_paths:
#                 video_files[folder] = paths

    # merge_videos(video_files, output_path)

@app.route('/<int:number>')
def render(number):

    out_dir = r'website/DataSet/Output/x'
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
    video_links = {}
    links = [os.path.join(out_dir, f) for f in os.listdir(
        out_dir) if f.endswith(video_extensions)]

    for i in range(1 ,len(links)):
        video_links[i] = links[i]

        def generate(video_path):
            with open(video_path, 'rb') as f:
                while True:
                    chunk = f.read(1024 * 1024)
                    if not chunk:
                        break
                    yield chunk

    return Response(generate(video_links[number]), mimetype='video/mp4')

if __name__ == '__main__':
    app.run()
