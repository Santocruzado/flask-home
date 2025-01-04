import os
from flask import Blueprint, render_template, current_app

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route('/new-home')
def new_home():
    images_dir = os.path.join(current_app.static_folder, 'images')
    images = [f"images/{img}" for img in os.listdir(images_dir) if img.endswith(("png", "jpg", "jpeg"))]

    
    return render_template("new-home.html", images=images)
