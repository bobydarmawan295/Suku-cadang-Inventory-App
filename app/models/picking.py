from app import db
from app.models.material import Material
from app.models.pekerjaan import Pekerjaan
from app.models.officer import Officer
from app.models.user import User
from datetime import datetime
from enum import Enum

class Status(Enum):
    PROSES = "Dalam proses"
    COMPLETE = "Selesai"
    FAILED = "batal"


class Picking(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tanggal= db.Column(db.DateTime, nullable=False, default=datetime.now)
    no_reservasi = db.Column(db.String(10), nullable=False, unique=True)
    jumlah_barang = db.Column(db.Integer, nullable=False)
    satuan = db.Column(db.String(10), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    id_material = db.Column(db.BigInteger, db.ForeignKey(Material.id))
    id_pekerjaan = db.Column(db.BigInteger, db.ForeignKey(Pekerjaan.id))
    id_officer = db.Column(db.BigInteger, db.ForeignKey(Officer.id))
    id_user = db.Column(db.BigInteger, db.ForeignKey(User.id))
    

    def __repr__(self):
        return '<Picking {}>'.format(self.name)



