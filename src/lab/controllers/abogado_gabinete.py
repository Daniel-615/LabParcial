from flask import jsonify, request

class AbogadoGabinete:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_abogado_gabinete(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)
            asociaciones = self.models.ABOGADO_GABINETE.query.order_by(self.models.ABOGADO_GABINETE.pasaporte).paginate(
                page=page, per_page=per_page, error_out=False
            )
            if not asociaciones.items:
                return jsonify({'message': 'No hay abogados asociados a ningún gabinete'}), 404

            return jsonify({
                'abogado_gabinete': [
                    {'pasaporte': ag.pasaporte, 'gabinete_id': ag.gabinete_id}
                    for ag in asociaciones.items
                ],
                'total': asociaciones.total,
                'pagina_actual': asociaciones.page,
                'total_paginas': asociaciones.pages
            }), 200

        except Exception as e:
            print("Error en get_abogado_gabinete:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def get_abogado_gabinete_by_id(self, id):
        try:
            abogados = self.models.ABOGADO_GABINETE.query.filter_by(gabinete_id=id).all()

            if not abogados:
                return jsonify({'message': 'No hay abogados registrados en ese gabinete'}), 404

            return jsonify([
                {'pasaporte': ag.pasaporte, 'gabinete_id': ag.gabinete_id}
                for ag in abogados
            ]), 200

        except Exception as e:
            print("Error en get_abogado_gabinete_by_id:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def create_abogado_gabinete(self, json_data):
        try:
            pasaporte = json_data.get('pasaporte')
            gabinete_id = json_data.get('gabinete_id')

            if not pasaporte or not gabinete_id:
                return jsonify({'message': "'pasaporte' y 'gabinete_id' son requeridos"}), 400

            # Validar existencia de abogado y gabinete
            abogado = self.models.ABOGADO.query.filter_by(pasaporte=pasaporte).first()
            gabinete = self.models.GABINETE.query.filter_by(id=gabinete_id).first()

            if not abogado or not gabinete:
                return jsonify({'message': 'Abogado o gabinete no encontrado'}), 404

            # Verificar si la relación ya existe
            existente = self.models.ABOGADO_GABINETE.query.filter_by(
                pasaporte=pasaporte, gabinete_id=gabinete_id
            ).first()

            if existente:
                return jsonify({'message': 'La asociación ya existe'}), 409

            nueva_asociacion = self.models.ABOGADO_GABINETE(
                pasaporte=pasaporte,
                gabinete_id=gabinete_id
            )
            self.db.session.add(nueva_asociacion)
            self.db.session.commit()

            return jsonify({
                'message': 'Asociación creada',
                'abogado_gabinete': {
                    'pasaporte': pasaporte,
                    'gabinete_id': gabinete_id
                }
            }), 201

        except Exception as e:
            print("Error en create_abogado_gabinete:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def update_abogado_gabinete(self, id, json_data):
        try:
            asociacion = self.models.ABOGADO_GABINETE.query.filter_by(gabinete_id=id).first()
            if not asociacion:
                return jsonify({'message': 'Asociación no encontrada'}), 404

            nuevo_pasaporte = json_data.get('pasaporte')
            if nuevo_pasaporte:
                # Validar si el nuevo pasaporte existe
                abogado = self.models.ABOGADO.query.filter_by(pasaporte=nuevo_pasaporte).first()
                if not abogado:
                    return jsonify({'message': 'Abogado no encontrado'}), 404

                asociacion.pasaporte = nuevo_pasaporte
                self.db.session.commit()

                return jsonify({
                    'message': 'Asociación actualizada',
                    'abogado_gabinete': {
                        'pasaporte': asociacion.pasaporte,
                        'gabinete_id': asociacion.gabinete_id
                    }
                }), 200

            return jsonify({'message': 'No se realizaron cambios'}), 400

        except Exception as e:
            print("Error en update_abogado_gabinete:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500
