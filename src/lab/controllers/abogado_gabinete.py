from flask import jsonify,request
class AbogadoGabinete:
    def __init__(self,db,models):
        self.db=db
        self.models=models
    def get_abogado_gabinete(self):
        page=request.args.get('page',default=1,type=int)
        per_page=request.args.get('per_page',default=10,type=int)

        all_abogado_gabinete=self.models.ABOGADO_GABINETE.query.paginate(page=page,per_page=per_page,error_out=False)
        if not all_abogado_gabinete.items:
            return jsonify({'message':'No hay abogados asociados a ningun gabinete'}),404
        else:
            return jsonify({
                'abogado_gabinete':[abogado.to_dict() for abogado in all_abogado_gabinete.items],
                'total':all_abogado_gabinete.total,
                'pagina_actual':all_abogado_gabinete.page,
                'total_paginas':all_abogado_gabinete.pages                        
            }),200
    def get_abogado_gabinete_by_id(self,id):
        abogado=self.models.ABOGADO_GABINETE.query.filter_by(gabinete_id=id).first()
        if not abogado:
            return jsonify({'message':'Abogado no encontrado'}),404
        else:
            return jsonify(
                abogado.to_dict()
                ),200
    def create_abogado_gabinete(self,json_abogado_gabinete):
        pasaporte=json_abogado_gabinete.get('pasaporte')
        gabinete_id=json_abogado_gabinete.get('gabinete_id')
        if not pasaporte or gabinete_id:
            return jsonify({
                'message':"'pasaporte' y 'gabinete_id' son requeridos"
            }),400
        abogado_gabinete=self.models.ABOGADO_GABINETE.query.filter_by(pasaporte=pasaporte).first()
        if abogado_gabinete:
            return jsonify({
                'message':'El gabinete para el abogado ya existe'
            }),400
        else:
            new_gabinete=self.models.ABOGADO_GABINETE(
                pasaporte=pasaporte,
                nombre=gabinete_id
            )
            self.db.session.add(new_gabinete)
            self.db.session.commit()
            return jsonify({
                'message':'Abogado creado',
                'abogado_gabinete':new_gabinete.to_dict()
            }),201
    def update_abogado_gabinete(self,id,json_abogado_gabinete):
        gabinete=self.models.ABOGADO_GABINETE.query.filter_by(gabinete_id=id).first()
        if not gabinete:
            return jsonify({
                'message':'gabinete no encontrado'
            }),404
        else:
            pasaporte=json_abogado_gabinete.get('pasaporte')
            if pasaporte:
                gabinete.pasaporte=pasaporte
                self.db.session.commit()
                return jsonify({
                    'message':'Abogado actualizado',
                    'gabinete':gabinete.to_dict()
                }),200
            else:
                return jsonify({
                    'message':'No se han realizado cambios'
                }),400