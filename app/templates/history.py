from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simulating an inventory and history log
inventory = {}
history = []  # List to store history of actions

@app.route('/')
def home():
    return render_template('index.html', inventory=inventory)

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form['name']
    quantity = int(request.form['quantity'])

    # Add item to inventory
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    
    # Record the action in the history
    history.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'item': item,
        'action': 'added',
        'quantity': quantity
    })

    return redirect(url_for('home'))

@app.route('/remove_item', methods=['POST'])
def remove_item():
    item = request.form['name']
    quantity = int(request.form['quantity'])

    # Remove item from inventory
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        if inventory[item] == 0:
            del inventory[item]
        
        # Record the action in the history
        history.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'item': item,
            'action': 'removed',
            'quantity': quantity
        })
    
    return redirect(url_for('home'))

@app.route('/history')
def view_history():
    return render_template('history.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)
