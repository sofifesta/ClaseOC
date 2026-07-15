from flask import flask, render_template 

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pajaros')
def pajaros():
    return render_template('pajaros.html')
                           
@app.route('/restaurante')                           
def restaurante():
    return render_template('restaurante.html')
                           
@app.route('/contactos')               
def contactos():     
    return render_template('contactos.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/artemis2videos')
def artemis2videos():
    return render_template('artemis2videos.html')

@app.route('/INSTRUCCIONES_DE_YOUTUBE')
def INSTRUCCIONES_DE_YOUTUBE():
    return ('INSTRUCCIONES_DE_YOUTUBE.HTML)')

if __name__ == "__main__":
 
    app.run(debug=True, port=5000)

