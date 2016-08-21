#!/usr/bin/python3
from src.api.ShapeShiftAPI import ShapeShiftAPI

class PostExchange(ShapeShiftAPI):
    """
    """
    def __init__(self):
        """
        """
        ShapeShiftAPI.__init__(self)

    def exchange(self, p = None,w = None,re = None,de = None,rs = None,api = None):
        """
        """
        return self.shapeshift_shift_request(pair = p, withdrawal = w, returnAddress = re, destTag = de, rsAddress = rs, apiKey = api)
