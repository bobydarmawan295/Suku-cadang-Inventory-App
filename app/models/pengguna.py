from app import db
from app.models.unit import Unit

class Pengguna(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    no_identitas = db.Column(db.String(25), nullable=False)
    no_hp = db.Column(db.String(20), nullable=False, unique=True)
    id_unit = db.Column(db.BigInteger, db.ForeignKey(Unit.id))

    def __repr__(self):
        return '<Officer {}>'.format(self.name)



