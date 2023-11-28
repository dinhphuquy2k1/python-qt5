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