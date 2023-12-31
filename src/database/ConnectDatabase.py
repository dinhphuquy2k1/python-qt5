from sqlalchemy import create_engine, text, update, or_
from sqlalchemy.orm import sessionmaker, joinedload

from src.models import OrderDetail
from src.models.base import Base
from src.views.common.Common import warningMessagebox
import configparser
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

    def deleteDataMutipleWithModel(self, model, ids):
        try:
            self.connect()
            self.session.query(model).filter(model.id.in_((ids))).delete()
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            return

        finally:
            self.close()

    def process_relation_with_request(self, relation, items):
        for model in relation:
            for item in items:
                if model.uuid == item.get('uuid'):
                    model.update(item)
                    self.session.commit()
                    break
            else:
                # If the item's uuid doesn't match any existing model, delete the model
                relation.remove(model)
                self.session.delete(model)
                self.session.commit()

        for item in items:
            if 'uuid' not in item:
                # If the item has no uuid, create a new model in the relation
                model_class = type(relation)
                new_model = model_class(**item)
                relation.append(new_model)
                self.session.commit()

    def insertDataMultipleWithModel(self, data):
        try:
            self.connect()
            self.session.bulk_save_objects(data)
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            return

        finally:
            self.close()

    # cập nhật bản ghi và thêm mới các bản ghi cho 1 relation
    def updateDataWithModelRelation(self, data, model, model_id, data_relation):
        try:
            self.connect()
            # query = update(model).where(model.id == model_id).values(data)
            # self.session.execute(query)
            self.session.merge(data)
            # thêm mới các bản ghi cho relation
            # self.session.bulk_save_objects(data_relation)
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            warningMessagebox("Đã xảy ra lỗi")
            self.session.rollback()
            return False
        finally:
            self.close()

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

    def updateOrInsert(self, data):
        try:
            self.connect()
            self.session.merge(data)
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
            query = update(model).where(model.id == model_id).values(data)
            self.session.execute(query)
            self.session.commit()
            return True
        except Exception as E:
            print(E)
            warningMessagebox("Đã xảy ra lỗi")
            self.session.rollback()
            return False
        finally:
            self.close()

    # Lấy thông tin bản ghi dựa vào model
    def getDataByIdWithModel(self, model, model_id):
        try:
            self.connect()
            result = self.session.query(model).options(joinedload('*')).filter_by(id=model_id).first()
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

    # Lấy ra bản ghi đầu tiên thỏa mãn điều kiện (bỏ qua bản ghi với id=model_id)
    def findFisrtWithColumnWithoutIdByModel(self, model, column, data, model_id):
        try:
            self.connect()
            return self.session.query(model).filter(column == data).filter(model.id != model_id).first()

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    # Lấy thông tin data dựa vào model
    def findFirstWithColumnByModel(self, model, column, data):
        try:
            self.connect()
            return self.session.query(model).filter(column == data).first()

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()

    def getDataByModelIdWithRelation(self, model, model_id):
        """
               Common function to get data from database.
               """
        try:
            self.connect()
            query = self.session.query(model).filter(model.id == model_id).options(joinedload('*'))
            result = query.distinct().order_by(model.created_at).first()
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
            query = self.session.query(model).options(joinedload('*'))
            result = query.distinct().order_by(model.created_at.desc()).all()
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

    # Tìm kiếm dữ liệu
    # model: Model muốn tìm kiếm
    # search_columns: danh sách cột muốn tìm kiếm. Ex: ['OtherColumn1', 'OtherColumn2']
    # searct_text: nội dung tìm kiếm
    # order_columns: các cột muốn sắp xếp. Ex: ['Status', 'CreatedDate']
    def searchData(self, model, search_columns, search_text, order_columns):
        try:
            # Xác định các cột sắp xếp
            order_by_columns = [getattr(model, col) for col in order_columns]
            # Tạo biểu thức điều kiện cho tìm kiếm
            search_conditions = [getattr(model, col).ilike(f"%{search_text}%") for col in search_columns]
            search_condition = or_(*search_conditions)
            self.connect()
            query = (
                self.session.query(model)
                .filter(search_condition)
                .order_by(*order_by_columns)
            )
            result = query.distinct().all()
            return result

        except Exception as E:
            print(E)
            return []

        finally:
            self.close()
