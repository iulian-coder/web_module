from flask import Flask, render_template, redirect, request

app = Flask(__name__)

save_data = {}

@app.route('/')
def route_index():
    note_text = None
    if 'note' in save_data:
        note_text = save_data['note']
    return render_template('index.html', note=note_text)


@app.route('/edit-note', methods=['GET', 'POST'])
def route_edit():
    if request.method == 'POST':
        save_data['note'] = request.form['note']
        return redirect('/')
    note_text = None
    if 'note' in save_data:
        note_text = save_data['note']
    return render_template('edit.html', note=note_text)

if __name__=='__main__':
    app.run(
        debug=True, port=5000
    )