#!/usr/bin/python3
from src.api.ShapeShiftAPI import ShapeShiftAPI

class ValidateAddress(ShapeShiftAPI):
    """
    """
    def __init__(self):
        ShapeShiftAPI.__init__(self)

    def validate(self, address = None, coin = None):
        """
        """
        return self.check_address(address = address, coin = coin)
