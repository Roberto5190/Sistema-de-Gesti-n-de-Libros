
"""
Blueprint de autenticación simple.
- Usuarios y contraseñas en memoria (solo demo).
- “Fake-JWT”: una cadena aleatoria guardada en un diccionario global.
"""

import secrets
from functools import wraps
from flask import Blueprint, request, jsonify, g
from models import Usuario, Moderador, Admin, login

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")
auth_bp.strict_slashes = False

# ---------------- Usuarios de ejemplo -----------------
USERS = {
    "alice": Usuario("alice", "secreto6"),
    "mod":   Moderador("mod", "modpass1"),
    "root":  Admin("root", "SuperAdmin1"),
}

# token → Usuario  (almacenados en memoria)
TOKENS: dict[str, Usuario] = {}



# ---------------- Helpers -----------------------------
def _json(data, code=200):
    return jsonify(data), code

def _generate_token() -> str:
    return secrets.token_urlsafe(24)



# ---------------- Decorador de roles ------------------
def role_required(*roles):
    """
    Protege una ruta verificando:
      - Encabezado Authorization: Bearer <token>
      - Que el token exista y el rol del usuario esté en roles permitidos.
    Ej.:  @role_required("admin", "moderator")
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            auth = request.headers.get("Authorization", "")
            if not auth.startswith("Bearer "):
                return _json({"error": "Token faltante"}, 401)
            token = auth.split(" ", 1)[1]
            user = TOKENS.get(token)
            if not user:
                return _json({"error": "Token inválido"}, 401)
            if roles and user.ROLE not in roles:
                return _json({"error": "Permiso denegado"}, 403)
            # Exponemos el usuario en flask.g por si la vista lo necesita
            g.current_user = user
            return fn(*args, **kwargs)
        return wrapper
    return decorator



# ---------------- Endpoint /login ---------------------
@auth_bp.post("/login")
def login_view():
    """
    Entrada:
      { "username": "...", "password": "..." }
    Respuesta:
      { "token": "<str>", "role": "<user|moderator|admin>" }
    """
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").lower()
    password = data.get("password", "")

    user = login(USERS, username, password)
    if not user:
        return _json({"error": "Credenciales inválidas"}, 401)

    # Generar/fetch token
    # (Opcional: reutilizar token existente para ese usuario)
    token = _generate_token()
    TOKENS[token] = user
    return _json({"token": token, "role": user.ROLE})
