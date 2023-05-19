from flask import Flask, request, render_template, redirect

app = Flask(__name__, static_folder='.', static_url_path='', template_folder='view')
items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/append', methods=['GET', 'POST'])
def append():
    if request.method == 'POST':
        append_data =request.form['todo_item'] 
        items.append(append_data)
        return render_template('append.html', item=append_data)
    else:
        return redirect('/')

@app.route('/see_all_item')
def see_all_item():
    return render_template('see_all_item.html', items=items)





app.run(port=8080, debug=True)
