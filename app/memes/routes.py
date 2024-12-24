from flask import Blueprint, current_app, send_from_directory, jsonify, url_for, render_template, request, abort
import os
import random

memes_bp = Blueprint('memes_bp', __name__, template_folder = '../templates/memes')

# GET all memes
@memes_bp.route('/get-memes')
def get_memes():
        images_dir = os.path.join(current_app.static_folder, 'images')
        images = [f"images/{img}" for img in os.listdir(images_dir) if img.endswith(("png", "jpg", "jpeg"))]
        
        return jsonify({"images": images})

@memes_bp.route('/imagenes')
def imagenes():
        return render_template('memes.html')