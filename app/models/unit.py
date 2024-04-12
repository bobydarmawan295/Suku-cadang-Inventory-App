from app import db

class Unit(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Unit {}>'.format(self.name)



