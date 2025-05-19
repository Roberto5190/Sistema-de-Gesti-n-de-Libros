"""
Blueprint CRUD para /api/libros
"""
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError # Importar la excepción de integridad
from models import LibroModel, db

from routes.auth import role_required

libros_bp = Blueprint('libros', __name__, url_prefix='/api/libros')

# ------------------ Helpers de serialización ------------------
def _json_ok(data, code=200):
    return jsonify(data), code # Respuesta JSON con código de estado




# ------------------ Endpoints CRUD ----------------------------
# GET /api/libros: devuelve todos los libros
@libros_bp.get('/')
def get_libros():
    libros = LibroModel.query.all()
    return _json_ok([l.to_dict() for l in libros])

# GET /api/libros/<int:id>: devuelve un libro por su ID
@libros_bp.get('/<int:id>')
def get_libro(id):
    libro = LibroModel.query.get_or_404(id) # SELECT * FROM libros WHERE id = <id>;
    return _json_ok(libro.to_dict())


# GET /api/libros/<string:titulo>: busca un libro por su título
@libros_bp.get('/<string:titulo>')
def get_libro_por_titulo(titulo):
    libro = LibroModel.query.filter_by(titulo=titulo).first_or_404() # SELECT * FROM libros WHERE titulo = <titulo>;
    return _json_ok(libro.to_dict())


# POST /api/libros: crea un nuevo libro
@libros_bp.post('/')
def create_libro():
    data = request.get_json(silent=True) or {} # Obtener datos del cuerpo de la solicitud
    if not data:
        return jsonify({'error': 'No se proporcionaron datos'}), 400
    
    # Validar que los campos requeridos estén presentes
    #    Aquí vas comprobando uno a uno y devolviendo 400 si falta algo.
    if not data.get("isbn"):
        return jsonify({"error": "El campo 'isbn' es obligatorio"}), 400
    if not data.get("titulo"):
        return jsonify({"error": "El campo 'titulo' es obligatorio"}), 400
    if not data.get("autor"):
        return jsonify({"error": "El campo 'autor' es obligatorio"}), 400
    # precio puede venir como string o número; compruebas primero que exista
    if "precio" not in data:
        return jsonify({"error": "El campo 'precio' es obligatorio"}), 400
    

    try:
        nuevo_libro = LibroModel(
            titulo = data['titulo'],
            autor = data['autor'],
            precio = float(data['precio']),
            stock = int(data.get('stock', 0)) # stock es opcional
        )
        db.session.add(nuevo_libro)
        db.session.commit()
        
    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Campos inválidos: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "El libro ya existe"}), 400    
    
    return _json_ok(nuevo_libro.to_dict(), 201)



# PUT /api/libros/<int:id>: actualiza el precio de un libro
@libros_bp.put('/<int:id>')
def update_libro(id):
    libro = LibroModel.query.get_or_404(id)
    data = request.get_json(silent=True) or {} # Obtener datos del cuerpo de la solicitud
    try:
           libro.update_from_dict(data)
           db.session.commit()
    except ValueError as e:
           return jsonify({"error": str(e)}), 400
    return _json_ok(libro.to_dict())


# DELETE /api/libros/<int:id>: elimina un libro
@libros_bp.delete('/<int:id>')
@role_required("admin")
def delete_libro(id):
    libro = LibroModel.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return '', 204
