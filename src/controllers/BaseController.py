from src.database.ConnectDatabase import ConnectMySQL
from mysql import connector

class BaseController:

    def __init__(self, model):
        self.connection = ConnectMySQL()
        self.model = model

    def getDataByModel(self):
        return self.connection.getDataByModel(self.model)

    def insertDataMultipleWithModel(self, data):
        return self.connection.insertDataMultipleWithModel(data)

    def getDataByQuery(self, query):
        return self.connection.getDataByQuery(query=query)

    def findFirstByQuery(self, query):
        return self.connection.findFirstByQuery(query=query)

    def insertData(self, data):
        return self.connection.insertData(data)

    def updateDataWithModel(self, data, model_id):
        return self.connection.updateDataWithModel(data, self.model, model_id)

    def updateDataWithQuery(self, data, query):
        return

    def getDataByIdWithModel(self, model_id):
        return self.connection.getDataByIdWithModel(self.model, model_id)

    def getDataByModelIdWithRelation(self, model_id):
        return self.connection.getDataByModelIdWithRelation(self.model, model_id)

    def deleteDataMutipleWithModel(self, ids):
        return self.connection.deleteDataMutipleWithModel(self.model, ids)

    def updateOrInsert(self, data):
        self.connection.updateOrInsert(data)

    def deleteDataWithModel(self, model, model_id):
        return self.connection.deleteDataWithModel(model, model_id)

    # kiểm tra data đã tồn tại khi insert
    def checkExitsDataWithModel(self, column, data):
        return self.connection.findFirstWithColumnByModel(self.model, column, data)

    # kiểm tra data đã tồn tại khi update
    def checkExitsDataUpdateWithModel(self, column, data, model_id):
        return self.connection.findFisrtWithColumnWithoutIdByModel(self.model, column, data, model_id)

    def searchData(self, search_column, search_text, order_columns=['created_at']):
        return self.connection.searchData(self.model, search_column, search_text, order_columns)