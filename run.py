from app import app, db
from app.models import Member, User

@app.shell_context_processor
def make_context():
    return dict(
        db=db,
        Member=Member,
        User=User
    )