from src.controllers.BaseController import BaseController
import re
from src.models.member_ranks import MemberRank
from src.models.images import Image


class MemberRankController(BaseController):

    def __init__(self):
        super().__init__(model=MemberRank)

