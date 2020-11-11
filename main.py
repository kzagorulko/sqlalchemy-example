from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DB_URL = URL(
    drivername='postgres',
    host='localhost',
    port=5432,
    username='sqlalchemy_demo_user',
    password='sqlalchemy_demo_user',
    database='sqlalchemy_demo'
)
engine = create_engine(DB_URL)  # echo=True

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return (
            f'<User id={self.id} name={self.name} fullname={self.fullname} '
            f'nickname={self.nickname}>'
        )


def get_users():
    users = session.query(UserModel).all()
    if users:
        print('\n'.join([str(user) for user in users]))
    else:
        print('User list is empty, add one!')


def create_user(name, fullname, nickname):
    user = UserModel(name=name, fullname=fullname, nickname=nickname)
    session.add(user)
    session.commit()
    print(f'Created! Id: {user.id}')


def get_user(user_id):
    user = session.query(UserModel).get(user_id)
    print(user)


def update_user(user_id, name=None, fullname=None, nickname=None):
    user = session.query(UserModel).get(user_id)
    user.name = name or user.name
    user.fullname = fullname or user.fullname
    user.nickname = nickname or user.nickname
    session.add(user)
    session.commit()
    print('Updated')


def delete_user(user_id):
    user = session.query(UserModel).get(user_id)
    session.delete(user)
    session.commit()
    print('Deleted')


if __name__ == '__main__':
    create_user('vova', 'vovachka', 'vovan')
    get_users()
