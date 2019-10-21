from ... import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    cod = db.Column(db.Integer, primary_key=True),
    
    nome = db.Column(db.String(100), unique=False, nullable=False),
    
    codpost = db.Column(db.Integer, db.ForeignKey('post.cod'),ondelete="cascade", onupdate="cascade")),
    
    # codcategoria em post


    def __init__(self,texto):
        self.nome = nome
        
    def salvar(categ):
        db.session.add(categ)
        db.session.commit()

    def listar():
        lista = Categoria.query.all()
        return lista

    def excluir(cod):
        Categoria.query.filter(Categoria.cod == cod).delete()
        db.session.commit()

    def buscar(cod):
        categ = Categoria.query.get(cod)
        return categ
