from flask_login import UserMixin

from apps import db, login_manager, supported_languages

from apps.authentication.util import hash_pass


class Users(db.Model, UserMixin):

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)
    language = db.Column(db.String(64))
    country = db.Column(db.String(64))
    tmdb_api = db.Column(db.String(64))

    def __init__(self, requets, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, "__iter__") and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == "password":
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

        for x in range(0, len(requets.best_match(supported_languages))):
            if requets.best_match(supported_languages)[x] == "-":
                language = requets.best_match(supported_languages)[0:x]
                country = requets.best_match(supported_languages)[
                    x + 1:len(requets.best_match(supported_languages))
                ]
                setattr(self, "language", language)
                setattr(self, "country", country)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    user = Users.query.filter_by(username=username).first()
    return user if user else None
