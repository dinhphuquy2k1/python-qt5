from src.controllers.BaseController import BaseController
import re
from src.models.orders import Order
from src.models.images import Image


class OrderController(BaseController):

    def __init__(self):
        super().__init__(model=Order)

