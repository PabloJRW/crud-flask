from flask import Flask, render_template
import os
#import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')


app = Flask(__name__, template_folder=template_dir)

# Rutas de la aplicación 
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True, port=5050)


#