from app import app
from flask import render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import os

# change to proper DB like SQL or some hosted service later.
inventory = {}

@app.route('/')
def home():
    return render_template('index.html', inventory=inventory)

@app.route('/add_item', methods=['POST'])
def add_item():
    item_name = request.form['name']
    quantity = int(request.form['quantity'])
    inventory[item_name] = inventory.get(item_name, 0) + quantity
    return redirect(url_for('home'))

@app.route('/scan_receipt', methods=['GET', 'POST'])
def scan_receipt():
    if request.method == 'POST':
        file = request.files['receipt']
        if file:
            file_path = os.path.join('static/images', file.filename)
            file.save(file_path)
            receipt_text = process_receipt(file_path)
            return render_template('receipt_scan.html', text=receipt_text)
    return render_template('scan_receipt.html')

def process_receipt(image_path):
    """Process the receipt image and extract text using Tesseract OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
