from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/Usuarios')
def Usuarios():
    return render_template('Usuarios.html')

@app.route('/Clientes')
def Clientes():
    return render_template('Clientes.html')

@app.route('/Proveedores')
def Proveedores():
    return render_template('Proveedores.html')

@app.route('/Productos')
def Productos():
    return render_template('Productos.html')

@app.route('/Ventas')
def Ventas():
    return render_template('Ventas.html')

@app.route('/Reportes')
def Reportes():
    return render_template('Reportes.html')


if __name__ == '__main__':
    app.run(debug=True)