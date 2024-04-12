from app import db

class Pekerjaan(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Pekerjaan {}>'.format(self.name)



