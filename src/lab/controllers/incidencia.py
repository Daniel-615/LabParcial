from flask import jsonify, request

class Incidencia:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_incidencias(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            incidencias = self.models.INCIDENCIA.query.order_by(self.models.INCIDENCIA.nombre).paginate(
                page=page, per_page=per_page, error_out=False)

            if not incidencias.items:
                return jsonify({'message': 'No hay incidencias registradas'}), 404

            return jsonify({
                'incidencias': [incidencia.to_dict() for incidencia in incidencias.items],
                'total': incidencias.total,
                'pagina_actual': incidencias.page,
                'total_paginas': incidencias.pages
            }), 200

        except Exception as e:
            print("Error en get_incidencias:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def get_incidencia_by_id(self, id):
        try:
            incidencia = self.models.INCIDENCIA.query.filter_by(id=id).first()

            if not incidencia:
                return jsonify({'message': 'Incidencia no encontrada'}), 404

            return jsonify(incidencia.to_dict()), 200

        except Exception as e:
            print("Error en get_incidencia_by_id:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def create_incidencia(self, json_data):
        try:
            audiencia_id = json_data.get('audiencia_id')
            descripcion = json_data.get('descripcion')

            if not audiencia_id or not descripcion:
                return jsonify({'message': "'audiencia_id' y 'descripcion' son requeridos"}), 400

            # Validar si la audiencia existe
            audiencia = self.models.AUDIENCIA.query.filter_by(id=audiencia_id).first()
            if not audiencia:
                return jsonify({'message': 'Audiencia no encontrada'}), 404

            nueva_incidencia = self.models.INCIDENCIA(
                audiencia_id=audiencia_id,
                descripcion=descripcion
            )
            self.db.session.add(nueva_incidencia)
            self.db.session.commit()

            return jsonify({
                'message': 'Incidencia creada',
                'incidencia': nueva_incidencia.to_dict()
            }), 201

        except Exception as e:
            print("Error en create_incidencia:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def update_incidencia(self, id, json_data):
        try:
            incidencia = self.models.INCIDENCIA.query.filter_by(id=id).first()

            if not incidencia:
                return jsonify({'message': 'Incidencia no encontrada'}), 404

            descripcion = json_data.get('descripcion')

            if descripcion:
                incidencia.descripcion = descripcion

            self.db.session.commit()

            return jsonify({
                'message': 'Incidencia actualizada',
                'incidencia': incidencia.to_dict()
            }), 200

        except Exception as e:
            print("Error en update_incidencia:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500
