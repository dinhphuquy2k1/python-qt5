from src.database.ConnectDatabase import ConnectMySQL
from mysql import connector

class BaseController:

    def __init__(self):
        self.connection = ConnectMySQL()

    def getDataByModel(self, model):
        return self.connection.getDataByModel(model=model)

    def getDataByQuery(self, query):
        return self.connection.getDataByQuery(query=query)

    def findFirstByQuery(self, query):
        return self.connection.findFirstByQuery(query=query)

    def insertData(self, data):
        return self.connection.insertData(data)

    def updateDataWithModel(self, data, model, model_id):
        return self.connection.updateDataWithModel(data, model, model_id)

    def updateDataWithQuery(self, data, query):
        return

    def getDataByIdWithModel(self, model, model_id):
        return self.connection.getDataByIdWithModel(model, model_id)


    def deleteDataWithModel(self, model, model_id):
        return self.connection.deleteDataWithModel(model, model_id)
