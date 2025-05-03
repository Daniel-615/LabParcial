from flask import request, jsonify

class Abogado:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_abogado(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            # Agregar order_by para evitar el error
            abogados = self.models.ABOGADO.query.order_by(self.models.ABOGADO.nombre).paginate(
                page=page, per_page=per_page, error_out=False
            )

            if not abogados.items:
                return jsonify({'message': 'No hay abogados registrados'}), 404

            return jsonify({
                "abogados": [a.to_dict() for a in abogados.items],
                "total": abogados.total,
                "pagina_actual": abogados.page,
                "total_paginas": abogados.pages,
            }), 200

        except Exception as e:
            print("Error en get_abogado:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def get_abogado_by_id(self, pasaporte):
        try:
            abogado = self.models.ABOGADO.query.filter_by(pasaporte=pasaporte).first()
            if not abogado:
                return jsonify({'message': 'Abogado no encontrado'}), 404

            return jsonify(abogado.to_dict()), 200

        except Exception as e:
            print("Error en get_abogado_by_id:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def create_abogado(self, json_abogado):
        try:
            pasaporte = json_abogado.get('pasaporte')
            nombre = json_abogado.get('nombre')

            if not pasaporte or not nombre:
                return jsonify({'message': "'pasaporte' y 'nombre' son obligatorios"}), 400

            if self.models.ABOGADO.query.filter_by(pasaporte=pasaporte).first():
                return jsonify({'message': 'Ya existe un abogado con ese pasaporte'}), 409

            nuevo_abogado = self.models.ABOGADO(
                pasaporte=pasaporte,
                nombre=nombre
            )
            self.db.session.add(nuevo_abogado)
            self.db.session.commit()

            return jsonify({
                "message": "Abogado creado correctamente",
                "abogado": nuevo_abogado.to_dict()
            }), 201

        except Exception as e:
            print("Error en create_abogado:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def update_abogado(self, pasaporte, json_abogado):
        try:
            abogado = self.models.ABOGADO.query.filter_by(pasaporte=pasaporte).first()
            if not abogado:
                return jsonify({'message': 'Abogado no encontrado'}), 404

            nuevo_nombre = json_abogado.get('nombre')
            if nuevo_nombre:
                abogado.nombre = nuevo_nombre
                self.db.session.commit()
                return jsonify({
                    "message": "Abogado actualizado correctamente",
                    "abogado": abogado.to_dict()
                }), 200

            return jsonify({'message': 'No se realizaron cambios'}), 400

        except Exception as e:
            print("Error en update_abogado:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500
