from sqlalchemy import Column, String, create_engine
from .base import Base, BaseMixin
from sqlalchemy.orm import sessionmaker
import configparser

class User(Base, BaseMixin):
    __tablename__ = 'users'
    username = Column(String(255), unique=True)
    name = Column(String(255))
    password = Column(String(255))

# tạo 1 tài khoản mặc định
def seeder_user():
    config = configparser.ConfigParser()
    config.read("alembic.ini")
    db_url = config.get("alembic", "sqlalchemy.url")
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    connection = None
    session = None
    try:
        # tạo 1 tài khoản mặc định
        connection = engine.connect()
        session = Session()
        session.add(User(username='0912229762', name='admin', password='1'))
        session.commit()

    except Exception as E:

        print("Không thể kết nối được database")

    finally:
        connection.close()
        session.close()

seeder_user()