from flask import Flask
from models import db  # Aquí se importa db de models/__init__.py
from routes.libros import libros_bp
from routes.auth import auth_bp


app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicializa SQLAlchemy con la aplicación
db.init_app(app)

# Registrar los Blueprints
app.register_blueprint(libros_bp)
app.register_blueprint(auth_bp)


# Modelo sencillo de ejemplo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    # Crear un usuario de ejemplo (una vez, para la demo)
    if not Usuario.query.first():
        nuevo_usuario = Usuario(nombre='Juan')
        db.session.add(nuevo_usuario)
        db.session.commit()
    usuarios = Usuario.query.all()
    return '<br>'.join([f'Usuario: {u.nombre}' for u in usuarios])

if __name__ == '__main__':
    # Crear todas las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)