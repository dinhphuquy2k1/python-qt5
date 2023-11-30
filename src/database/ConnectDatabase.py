from sqlalchemy import create_engine, text, update
from sqlalchemy.orm import sessionmaker
from src.models.base import Base
import configparser
from src.models.users import User

class ConnectMySQL:
    def __init__(self, config_file_path="alembic.ini"):
        config = configparser.ConfigParser()
        config.read(config_file_path)
        db_url = config.get("alembic", "sqlalchemy.url")

        # Tạo engine và kết nối đến cơ sở dữ liệu
        try:
            self.engine = create_engine(db_url)
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)

        except Exception as E:

            print("Không thể kết nối được database")

        self.connection = None
        self.session = None

    def connect(self):
        """
        Connect to MySQL Database.
        """
        self.connection = self.engine.connect()
        self.session = self.Session()

    def close(self):
        self.connection.close()
        self.session.close()

    def findFirstByQuery(self, query):
        self.connect()
        try:
            query = self.session.execute(text(query))
            result = query.first()
            return result

        except Exception as E:
            print(E)
            return

        finally:
            self.close()

    def insertData(self, data):
        try:
            self.connect()
            self.session.add(data)
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            self.session.rollback()
            return False
        finally:
            self.close()

    def updateDataWithQuery(self, query):
        return

    # cập nhật thông tin bản ghi
    def updateDataWithModel(self, data, model, model_id):
        try:
            self.connect()
            query = update(User).where(model.id == model_id).values(data)
            self.session.execute(query)
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            self.session.rollback()
            return False
        finally:
            self.close()

    # Lấy thông tin bản ghi dựa vào model
    def getDataByIdWithModel(self, model, model_id):
        try:
            self.connect()
            result = self.session.query(model).filter_by(id=model_id).first()
            return result

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    # Xóa bản ghi
    def deleteDataWithModel(self, model, model_id):
        try:
            self.connect()
            self.session.query(model).filter_by(id=model_id).delete()
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            return []

        finally:
            self.close()


    def getDataByIdWithQuery(self, model_id):
        try:
            self.connect()
            result = []
            print(result)
            return result

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    def getDataByQuery(self, query):
        self.connect()
        try:
            result = self.session.execute(text(query)).fetchall()
            return result

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    def findFirstByModel(self, model, filters=None):
        self.connect()
        try:
            query = self.session.query(model)
            result = query.all()
            return result

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    def getDataByModel(self, model):
        """
        Common function to get data from database.
        """
        try:
            self.connect()
            query = self.session.query(User)
            result = query.distinct().all()
            return result

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    def update_data(self, data):
        """
        Common function to update database.
        """
        self.connect()
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as E:
            self.session.rollback()
            return E
        finally:
            self.session.close()

    ## function for login window
    def create_login_account(self, user_name, password):
        """
        Insert new login account data
        """
        sql = f"INSERT INTO user_tb (user_name, password) VALUES ('{user_name}', '{password}')"

        result = self.update_data(sql=sql)

        return result

    def check_username(self, username):
        """
        Check the username when create new login account.
        """
        sql = f"SELECT * FROM user_tb WHERE user_name='{username}'"

        result = self.get_data(sql=sql)

        return result

    ## Function for show data window
    def get_password_list(self, user_id, search_username, search_website):
        """
        Search and get password data from database.
        """
        sql = f"""
            SELECT * FROM password_tb 
                WHERE user_id={user_id} 
                    AND user_name LIKE '%{search_username}%'
                    AND website LIKE '%{search_website}%';
        """

        result = self.get_data(sql=sql)

        return result

    def delete_password_data(self, id):
        """
        Delete selected password data from database.
        """
        sql = f"DELETE FROM password_tb WHERE id={id}"

        result = self.update_data(sql=sql)

        return result

    ## Function for generate password window
    def save_new_password(self, user_id, user_name, website, password):
        """
        Save the new generate password data
        """
        sql = f"""
            INSERT INTO password_tb (user_id, user_name, website, password)
                VALUES ({user_id}, '{user_name}', '{website}', '{password}');
        """

        result = self.update_data(sql=sql)

        return result

    ## function for configuration window
    def create_config_data(self, user_id,
                           lowercase="abcdefghijklmnopqrstuvwxyz",
                           uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                           numbers="1234567890",
                           special_characters="@#$%&^!"):
        """
        Create configuration data for special account
        """
        sql = f"""
            INSERT INTO configuration_tb (user_id, lowercase, uppercase, numbers, special_characters )
	            VALUES ({user_id}, '{lowercase}', '{uppercase}', '{numbers}', '{special_characters}');
        """

        result = self.update_data(sql=sql)

        return result

    def check_config_data(self, user_id):
        """
        Check if the configuration data for the user is in the database.
        """
        sql = f"SELECT * FROM configuration_tb WHERE user_id={user_id}"

        result = self.get_data(sql=sql)

        return result

    def update_config_data(self, user_id, lowercase, uppercase, numbers, special_characters):
        """
        Update configuration data.
        """
        sql = f"""
            UPDATE configuration_tb 
                SET lowercase='{lowercase}', uppercase='{uppercase}',
                    numbers='{numbers}', special_characters='{special_characters}'
                WHERE user_id={user_id}
        """

        result = self.update_data(sql=sql)

        return result
