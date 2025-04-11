from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__= 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(25), nullable=False)
    last_name: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    comments: Mapped[list['Comment']] = relationship(back_populates='comment_by')
    posts: Mapped[list['Post']] = relationship(back_populates='author')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Follower(db.Model):
    __tablename__= 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    url: Mapped[str] = mapped_column(String(20), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    post: Mapped['Post'] = relationship(back_populates='media', uselist=False)
    

class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    media: Mapped['Media'] = relationship(back_populates='post', uselist=False)
    

class Comment(db.Model):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(20), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id')) 
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))  
    comment_by: Mapped['User'] = relationship(back_populates=('comments'))