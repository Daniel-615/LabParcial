from flask import jsonify, request

class AbogadoGabinete:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_abogado_gabinete(self):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        all_abogado_gabinete = self.models.ABOGADO_GABINETE.query.paginate(page=page, per_page=per_page, error_out=False)

        if not all_abogado_gabinete.items:
            return jsonify({'message': 'No hay abogados asociados a ningún gabinete'}), 404

        return jsonify({
            'abogado_gabinete': [
                {'pasaporte': ag.pasaporte, 'gabinete_id': ag.gabinete_id}
                for ag in all_abogado_gabinete.items
            ],
            'total': all_abogado_gabinete.total,
            'pagina_actual': all_abogado_gabinete.page,
            'total_paginas': all_abogado_gabinete.pages
        }), 200

    def get_abogado_gabinete_by_id(self, id):
        abogados = self.models.ABOGADO_GABINETE.query.filter_by(gabinete_id=id).all()
        if not abogados:
            return jsonify({'message': 'No hay abogados registrados en ese gabinete'}), 404

        return jsonify([
            {'pasaporte': ag.pasaporte, 'gabinete_id': ag.gabinete_id}
            for ag in abogados
        ]), 200

    def create_abogado_gabinete(self, json_abogado_gabinete):
        pasaporte = json_abogado_gabinete.get('pasaporte')
        gabinete_id = json_abogado_gabinete.get('gabinete_id')

        if not pasaporte or not gabinete_id:
            return jsonify({'message': "'pasaporte' y 'gabinete_id' son requeridos"}), 400

        existente = self.models.ABOGADO_GABINETE.query.filter_by(
            pasaporte=pasaporte,
            gabinete_id=gabinete_id
        ).first()

        if existente:
            return jsonify({'message': 'La relación ya existe'}), 409

        nuevo = self.models.ABOGADO_GABINETE(
            pasaporte=pasaporte,
            gabinete_id=gabinete_id
        )
        self.db.session.add(nuevo)
        self.db.session.commit()

        return jsonify({
            'message': 'Asociación creada',
            'abogado_gabinete': {'pasaporte': pasaporte, 'gabinete_id': gabinete_id}
        }), 201

    def update_abogado_gabinete(self, id, json_abogado_gabinete):
        gabinete = self.models.ABOGADO_GABINETE.query.filter_by(gabinete_id=id).first()
        if not gabinete:
            return jsonify({'message': 'Gabinete no encontrado'}), 404

        pasaporte = json_abogado_gabinete.get('pasaporte')
        if pasaporte:
            gabinete.pasaporte = pasaporte
            self.db.session.commit()
            return jsonify({
                'message': 'Asociación actualizada',
                'gabinete': {'pasaporte': gabinete.pasaporte, 'gabinete_id': gabinete.gabinete_id}
            }), 200

        return jsonify({'message': 'No se realizaron cambios'}), 400
