from flask import Flask, render_template , send_file
from flask_bootstrap import Bootstrap5
from image_info import image_info
from PIL import Image, ImageOps 
import random

app = Flask(__name__)

import random
from flask import Flask, render_template
from image_info import image_info

app = Flask(__name__)

import random
from flask import Flask, render_template
from image_info import image_info
from PIL import Image

app = Flask(__name__)

def get_random_images(image_info):
    shuffled_images = image_info[:] 
    random.shuffle(shuffled_images)
    selected_images = shuffled_images[:3]
    image_data = []
    for image in random_images:
        image_id = image["id"]
        title = image["title"]
        author = image["flickr_user"]
        image_data.append({ "id": image_id, "title": title, "author": author})
    return image_data

@app.route('/')
def index():
    random_image_data = get_random_images(image_info)
    return render_template('index.html', images=random_image_data)

@app.route('/picture/[image_id]')
def ran_img():
    image_path = f'static/images/{image_id}.jpg'
    img = Image.open(image_path)
    pic_info = {"mode": img.mode, "format": img.format,"height": img.height, "width": img.width}
    return render_template('detail.html',pic_info=pic_info)
   
bootstrap = Bootstrap5(app)