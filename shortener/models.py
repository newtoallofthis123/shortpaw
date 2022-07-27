from shortener import app, db

class Bin(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer(), primary_key=True)
    og_url = db.Column(db.Text())
    hash = db.Column(db.Text())
    time = db.Column(db.String())

    def __init__(self, og_url, hash, time):
        self.og_url = og_url
        self.hash = hash
        self.time = time

    def __repr__(self):
        return '<id {}>'.format(self.id)