from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from image_info import image_info
from PIL import Image
import os
import random
#name: Jessika Torrealba
#class:CST205
# date: 08 Nov 2024
# comment: none

app = Flask(__name__)


def get_random_images_from_static(static_folder, image_info, num_images=3):
    # Get all image files from the static folder
    image_files = [f for f in os.listdir(static_folder) if f.endswith('.jpg')]
    random.shuffle(image_files)
    selected_images = image_files[:num_images]
    image_data = []
    for image_file in selected_images:
        image_id = os.path.splitext(image_file)[0]
        image_info_data = next((img for img in image_info if img["id"] == image_id), None)
        if image_info_data:
            title = image_info_data["title"]
            author = image_info_data["flickr_user"]
            image_data.append({"id": image_id, "title": title, "author": author})
    return image_data

@app.route('/')
def index():
    static_folder = 'static'
    random_image_data = get_random_images_from_static(static_folder, image_info)
    return render_template('index.html', images=random_image_data)

@app.route('/picture/<image_id>')
def ran_img(image_id):
    image_info_data = next((img for img in image_info if img["id"] == image_id), None)
    image_path = f'static/{image_id}.jpg'
    img = Image.open(image_path)
    pic_info = {"mode": img.mode, "format": img.format, "height": img.height, "width": img.width}
    return render_template('detail.html', image=image_info_data, pic_info=pic_info)

bootstrap = Bootstrap5(app)


