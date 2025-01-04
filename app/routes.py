import os
from flask import Blueprint, render_template, current_app, jsonify

main = Blueprint('main', __name__)


@main.route('/')
def home():
    images_dir = os.path.join(current_app.static_folder, 'images')
    images = [f"images/{img}" for img in os.listdir(images_dir) if img.endswith(("png", "jpg", "jpeg"))]

    
    return render_template("home.html", images=images)

@main.route('/meme-images')
def get_meme_images():
    images_dir = os.path.join(current_app.static_folder, 'images')
    images = [f"images/{img}" for img in os.listdir(images_dir) if img.endswith(("png", "jpg", "jpeg"))]

    return jsonify({"images": images})