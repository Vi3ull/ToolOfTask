from app import db, session, Base

class Todo(Base):
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  description = db.Column(db.String(500), nullable=False)
  status = db.Column(db.Boolean, default=False)