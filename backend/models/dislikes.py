from app import db, ma
from models.base import BaseModel
from marshmallow import fields, post_load
# from models.user import User
class Dislike(db.Model, BaseModel):
  __tablename__ = 'dislikes'
  disliked_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
  disliker_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
  user_relationship = db.relationship('User', foreign_keys=[disliker_id], backref='dislikes')

