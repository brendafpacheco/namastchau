from ... import db

class Comentario(db.Model):
    __tablename__ = 'comentario'
    cod = db.Column(db.Integer, primary_key=True),
    
    texto = db.Column(db.String(10000), unique=False, nullable=False),
    
    datahora = db.Column(db.Date, unique=False, nullable=False),
    
    codpost = db.Column(db.Integer, db.ForeignKey('post.cod'),ondelete="cascade", onupdate="cascade")),
    
    codusuario = db.Column(db.Integer, db.ForeignKey('usuario.cod'),ondelete="cascade", onupdate="cascade"))

    def __init__(self,texto,datahora):
        self.texto = texto
        self.datahora = datahora

    def salvar(coment):
        db.session.add(coment)
        db.session.commit()

    def listar():
        lista = Comentario.query.all()
        return lista

    def excluir(cod):
        Comentario.query.filter(Comentario.cod == cod).delete()
        db.session.commit()

    def buscar(cod):
        coment = Comentario.query.get(cod)
        return coment
