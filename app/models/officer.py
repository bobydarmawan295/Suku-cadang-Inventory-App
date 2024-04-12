from app import db

class Officer(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    no_identitas = db.Column(db.String(25), nullable=False)
    nama = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<Officer {}>'.format(self.name)



