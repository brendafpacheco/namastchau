from ... import db

class Post(db.Model):
    __tablename__ = 'post'
    cod = db.Column(db.Integer, primary_key=True),
    
    titulo = db.Column(db.String(1000), unique=False, nullable=False),
    
    texto = db.Column(db.String(100000), unique=False, nullable=False),
    
    datahora = db.Column(db.Date, unique=False, nullable=False),
    
    comentarios = db.relationship('Comentario', backref= 'post', lazy = 'select'),
    
    categoria = db.relationship('Categoria', backref='post', lazy = 'select')
    
    def __init__(self,titulo,texto,datahora):
        self.titulo = titulo
        self.texto = texto
        self.datahora = datahora

    def salvar(p):
        db.session.add(p)
        db.session.commit()

    def listar():
        lista = Post.query.all()
        return lista

    # def listaCateg():
    #     lista = Comentario.query.all()
    
    def excluir(cod):
        Post.query.filter(Post.cod == cod).delete()
        db.session.commit()

    def buscar(cod):
        po = Post.query.get(cod)
        return po

