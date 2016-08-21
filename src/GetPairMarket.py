#!/usr/bin/python3
from src.api.ShapeShiftAPI import ShapeShiftAPI

class GetPairMarket(ShapeShiftAPI):
    """
    """
    def __init__(self):
        """
        """
        ShapeShiftAPI.__init__(self)

    def get_pair_market_info(self, pair = None):
        """
        """
        return self.return_shapeshift_market(pair = pair)

if __name__ == '__main__':
    app = GetPairMarket()
    print(app.get_pair_market_info(pair = "BTC_LTC"))
