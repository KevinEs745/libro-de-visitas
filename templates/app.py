from flask import Flask, render_template, request, redirect

app = Flask(__name__)
mensajes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        mensaje = request.form['mensaje']
        mensajes.append({'nombre': nombre, 'mensaje': mensaje})
        return redirect('/')
    return render_template('index.html', mensajes=mensajes)

if __name__ == '__main__':
    app.run(debug=True)
