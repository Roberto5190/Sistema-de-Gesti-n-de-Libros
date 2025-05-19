# routes/libros.py
from flask import Blueprint, request, jsonify
from models import LibroModel, db

libros_bp = Blueprint('libros', __name__)

# GET /api/libros: devuelve todos los libros
@libros_bp.route('/api/libros', methods=['GET'])
def get_libros():
    libros = LibroModel.query.all()
    return jsonify([{
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'precio': libro.precio
    } for libro in libros])

# POST /api/libros: crea un nuevo libro
@libros_bp.route('/api/libros', methods=['POST'])
def create_libro():
    data = request.get_json()
    titulo = data.get('titulo')
    autor = data.get('autor')
    precio = data.get('precio')

    # Validar que el precio sea mayor o igual a 0
    if precio < 0:
        return jsonify({'error': 'El precio no puede ser negativo'}), 400

    # Crear el libro y agregarlo a la base de datos
    nuevo_libro = LibroModel(titulo=titulo, autor=autor, precio=precio)
    db.session.add(nuevo_libro)
    db.session.commit()
    
    return jsonify({
        'id': nuevo_libro.id,
        'titulo': nuevo_libro.titulo,
        'autor': nuevo_libro.autor,
        'precio': nuevo_libro.precio
    }), 201

# GET /api/libros/<int:id>: devuelve un libro por su ID
@libros_bp.route('/api/libros/<int:id>', methods=['GET'])
def get_libro(id):
    libro = LibroModel.query.get_or_404(id)
    return jsonify({
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'precio': libro.precio
    })

# PUT /api/libros/<int:id>: actualiza el precio de un libro
@libros_bp.route('/api/libros/<int:id>', methods=['PUT'])
def update_libro(id):
    libro = LibroModel.query.get_or_404(id)
    data = request.get_json()
    precio = data.get('precio')

    # Validar que el precio sea mayor o igual a 0
    if precio < 0:
        return jsonify({'error': 'El precio no puede ser negativo'}), 400
    
    libro.precio = precio
    db.session.commit()
    return jsonify({
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'precio': libro.precio
    })

# DELETE /api/libros/<int:id>: elimina un libro
@libros_bp.route('/api/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    libro = LibroModel.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return '', 204
