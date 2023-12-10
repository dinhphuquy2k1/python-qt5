from src.controllers.BaseController import BaseController
import re
from src.models.customers import Customer
from src.models.images import Image


class CustomerController(BaseController):

    def __init__(self):
        super().__init__(model=Customer)

