from flask.cli import FlaskGroup
from app import create_app
from app.models import db, User, Vote

app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(name="juan", password="juan", email="j@j.com"))
    db.session.commit()

@cli.command("seed_db2")
def seed_db():
    db.session.add(Vote(name="dave", user_id=1))
    db.session.commit()

if __name__ == "__main__":
    cli()