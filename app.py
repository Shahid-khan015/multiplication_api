from flask import Flask, Response , jsonify
import os
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

application = app

out_dir = r'website/DataSet/Output/x'
video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
video_links = {}
links = [os.path.join(out_dir, f) for f in os.listdir(out_dir) if f.endswith(video_extensions)]
for i in range(1 ,len(links)):
    video_links[i] = links[i]


@app.route('/')
def home():
    return jsonify(video_links)



@app.route('/<int:number>')
def render(number):
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
