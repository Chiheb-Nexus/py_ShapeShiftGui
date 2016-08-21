#!/usr/bin/python3
from src.api.ShapeShiftAPI import ShapeShiftAPI

class GetCoinSymbol(ShapeShiftAPI):
    """
    """
    def __init__(self):
        """
            Initialize
        """
        ShapeShiftAPI.__init__(self)

    def get_symbol_of_coin(self, coin = None):
        """
            Return the symbol of an input coin name
            Example: input = "Bitcoin" => output = "BTC"
        """
        if coin != None:
            coin = coin[:1].upper() + coin[1:]

            # DEBUG
            print("GetCoinSymbol: coin =", coin)
            
            coins = self.get_coins_name_symbol()
            for x in coins:
                if x[0] == coin:
                    return x[1]
        else:
            return None

    def get_coins_name_symbol(self):
        """
            Return all supported Shapeshift coins
        """
        coins = list((self.return_shapeshift_coins()).values())
        return [(x["name"], x["symbol"]) for x in coins]


if __name__ == '__main__':
    app = GetCoinSymbol()
    symb = app.get_symbol_of_coin(coin = "bitcoin")
    print("symbol: ", symb)
