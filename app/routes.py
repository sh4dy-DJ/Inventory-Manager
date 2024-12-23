# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import os

# Create a Blueprint for modularity (can have multiple blueprints in a larger app)
main = Blueprint('main', __name__)

# Placeholder for inventory (could be a database in a real app)
inventory = {}

# Route for the home page
@main.route('/')
def home():
    return render_template('index.html', inventory=inventory)

# Route for adding an item to the inventory
@main.route('/add_item', methods=['POST'])
def add_item():
    item_name = request.form['name']
    quantity = int(request.form['quantity'])
    inventory[item_name] = inventory.get(item_name, 0) + quantity
    return redirect(url_for('main.home'))

# Route for scanning the receipt
@main.route('/scan_receipt', methods=['GET', 'POST'])
def scan_receipt():
    if request.method == 'POST':
        file = request.files['receipt']
        if file:
            file_path = os.path.join('static/images', file.filename)
            file.save(file_path)
            receipt_text = process_receipt(file_path)
            return render_template('receipt_scan.html', text=receipt_text)
    return render_template('scan_receipt.html')

# Helper function for OCR text extraction
def process_receipt(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

@main.route('/inventory')
def inventory_page():
    return render_template('inventory.html', inventory=inventory)
