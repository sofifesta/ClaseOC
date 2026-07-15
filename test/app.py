from flask import Flask

# 1. Inicializamos la aplicación Flask
app = Flask(__name__)

# 2. Definimos una "ruta". 
# Esto le dice a Flask qué hacer cuando alguien entra a la página principal ('/')
@app.route("/")
def home():
    return "<h1>¡Hola Mundo desde Flask!</h1><p>Esta es mi primera página web con Python.</p>"

# 3. Definimos otra ruta para probar
@app.route("/contacto")
def contacto():
    return "<h2>Página de contacto</h2><p>Escríbenos a contacto@ejemplo.com</p>"

# 4. Ejecutamos la aplicación (Solo si este archivo se ejecuta directamente)
# Nota: En un entorno real se evita ejecutar app.run() directamente en producción, 
# pero para practicar está perfecto.
if __name__ == "__main__":
    # debug=True permite que el servidor se reinicie si hacemos cambios en el código
    # IMPORTANTE: No ejecutar esta celda dentro de Jupyter, ya que bloqueará el notebook.
    # Mejor copia este código a un archivo app.py y ejecútalo en la terminal.
    app.run(debug=True, port=5000)
