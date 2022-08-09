from shortener import app, db

class Bin(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer(), primary_key=True)
    og_url = db.Column(db.Text())
    hash = db.Column(db.Text())
    visits  = db.Column(db.Integer())
    time = db.Column(db.String())

    def __init__(self, og_url, visits, hash, time):
        self.og_url = og_url
        self.hash = hash
        self.visits = visits
        self.time = time

    def __repr__(self):
        return '<id {}>'.format(self.id)
