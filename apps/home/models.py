from apps import db

class Watchlist(db.Model):

    __tablename__ = "Watchlist"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,nullable=False)
    tmdbId = db.Column(db.Integer,db.ForeignKey('Users.id'),nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)

    def __repr__(self):
        return str(self.userId)

class Watched(db.Model):

    __tablename__ = "Watched"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,nullable=False)
    tmdbId = db.Column(db.Integer,db.ForeignKey('Users.id'),nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)

    def __repr__(self):
        return str(self.userId)

