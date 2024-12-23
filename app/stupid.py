from flask import Blueprint, current_app, send_from_directory, jsonify, url_for, render_template
import os
import random

# Crear el blueprint
stupid_bp = Blueprint('stupid_bp', __name__)

@stupid_bp.route('/stupid-image')
def get_random_image():
    images_dir = os.path.join(current_app.static_folder, 'images')
    images = os.listdir(images_dir)
    selected_image = random.choice(images)    
    image_url = url_for('static', filename=f'images/{selected_image}')    

    return jsonify({"url": image_url})

@stupid_bp.route('/stupid')
def stupid():
        return render_template('stupid.html')

@stupid_bp.route('/meme')
def meme():
    images_dir = os.path.join(current_app.static_folder, 'images')
    images = [f"images/{img}" for img in os.listdir(images_dir) if img.endswith(("png", "jpg", "jpeg"))]

    return render_template('meme.html', images=images)