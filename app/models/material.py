from app import db

class Material(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    material_code = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(50), nullable=False)
    satuan = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Material {}>'.format(self.name)



