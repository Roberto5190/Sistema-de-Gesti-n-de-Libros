# routes/auth.py
from flask import Blueprint, request, jsonify
from models.usuario import Usuario, Moderador, Admin, login

auth_bp = Blueprint('auth', __name__)

# POST /api/login: autenticar al usuario según su rol
@auth_bp.route('/api/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')  # Rol: "user", "moderador" o "admin"

    # Crear instancia del usuario según el rol
    if role == "moderador":
        usuario = Moderador(username, password)
    elif role == "admin":
        usuario = Admin(username, password)
    else:
        usuario = Usuario(username, password)

    # Intentar autenticar
    if login(usuario, password):
        return jsonify({'token': 'fake-jwt'}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401
