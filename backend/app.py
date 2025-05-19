from flask import Flask, jsonify
from flask_cors import CORS
from models import db  # Aquí se importa db de models/__init__.py


# ——————————————————————————————
# 1. Crear la app Flask y configurar la base de datos
# ——————————————————————————————
app = Flask(__name__)

# Configuración de la base de datos SQLite
# 1) Configurar la URL de la base (aquí, un archivo SQLite local)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
# 2) Tracking de modificaciones desactivado (opcional)
# Esto evita advertencias de SQLAlchemy sobre el seguimiento de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicializa SQLAlchemy con la aplicación
db.init_app(app)


# ---- CORS ----
CORS(app, origins=["http://localhost:5173"], supports_credentials=False)


# Registrar los Blueprints
from routes.libros import libros_bp
from routes.auth import auth_bp

app.register_blueprint(libros_bp)
app.register_blueprint(auth_bp)




# --- manejo de errores ---
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(ValueError)
def bad_request(e):
    return jsonify({"error": str(e)}), 400




# --- Rutas de ejemplo ---
# Esta ruta es solo un ejemplo para mostrar cómo funciona la base de datos
# ——————————————————————————————
# 2. Definir el modelo Usuario
#    Cada instancia corresponde a una fila en la tabla 'usuario'
# ——————————————————————————————
# Modelo sencillo de ejemplo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    # Crear un usuario de ejemplo (una vez, para la demo)
    if not Usuario.query.first():
        nuevo_usuario = Usuario(nombre='Juan') # crea instancia
        db.session.add(nuevo_usuario)          # agrega a la sesión
        db.session.commit()                    # guarda cambios / ejecuta INSERT en la BD
    
    
    usuarios = Usuario.query.all()     # Recuperar todos los usuarios de la base de datos //# SELECT * FROM usuario
    return '<br>'.join([f'Usuario: {u.nombre}' for u in usuarios])  # y devolverlos como una lista de cadenas


# ——————————————————————————————
# 4. Crear la tabla en la base de datos
#    (Se ejecuta al iniciar la app; en producción usar migraciones)
#     -> python app.py
# ——————————————————————————————
if __name__ == '__main__':
    # Crear todas las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)