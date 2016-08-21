#!/usr/bin/python3
# ShapeShiftAPI : Complete API wrapper for shapeshift.io
#
# Copyright © 2016 Chiheb Nexus
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
##########################################################################################

from urllib.request import urlopen, Request
from json import loads, dumps

class ShapeShiftAPI(object):
	"""
	This is a complete ShapeShift API wrapper using HTTP/1.1
	For more informations Please visit ShapeShift API website: https://info.shapeshift.io/api

	"""
	def __init__(self):
		"""
		Initialize urls
		"""
		self.url_rate = "https://shapeshift.io/rate/"
		self.url_limit = "https://shapeshift.io/limit/"
		self.url_market = "https://shapeshift.io/marketinfo/"
		self.url_coins = "https://shapeshift.io/getcoins"
		self.url_valid_address = "https://shapeshift.io/validateAddress/"
		self.url_post_exchange = "https://shapeshift.io/shift/"
		self.url_request_mail = "https://shapeshift.io/mail/"
		self.url_post_exchange_fixed = "https://shapeshift.io/sendamount/"
		self.url_cancel_pending = "https://shapeshift.io/cancelpending/"
		self.url_tx_status = "https://shapeshift.io/txStat/"
		self.url_tx_timeleft = "https://shapeshift.io/timeremaining/"

	def shapeshift_fixed_tx_timeleft(self, adress = None):
		"""
		@input:
			adress : is the deposit address to look up.
			NOTE: This request is valid only for fixed amount transaction

		@return (if success): example:
			{"status":"pending","seconds_remaining":"577"}
		@return (if failure):
			{'error': 'Unable to find pending transaction'}
		"""
		if adress != None:
			__url = self.url_tx_timeleft+adress
			return self.load_url(__url)
		else:
			print("Usage: ShapeShiftAPI.shapeshift_fixed_tx_timeleft(adress = 'Your adress')")
			return None

	def shapeshift_shift_tx_status(self, address = None, apiKey = None):
		"""
		@input:
			adress : (Required) the address that output coin was sent to for the shift
			apiKey : (Optional) is the affiliate's PRIVATE api key
		@return (if success):
			{'status': 'no_deposits', 'address': '19533VePoBBsceTztqmtRgjVkMKHCta6UR'} // or status = deposit
		@return (if failure):
			{'address': '19533VePoBBsceTztqmtRgjVkMKHCta6URs',
			 'error': 'This address is NOT a ShapeShift deposit address.
			  Do not send anything to it.', 'status': 'error'}
		"""
		if address != None and apiKey != None:
			__url = self.url_tx_status+address+"/"+apiKey
			return self.load_url(__url)
		elif address != None and apiKey == None:
			__url = self.url_tx_status+address
			return self.load_url(__url)
		else:
			print("Usage:")
			return None

	def shapeshift_cancel_pending_tx(self, address = None):
		"""
		@FIXME: Not working
		"""
		__url = self.url_cancel_pending
		if adress != None:
			__post_data = {"address": address}
			return self.post_exchange(url = __url, post_data = __post_data)
		else:
			print("Usage:")
			return None

	def shapeshift_shift_request_fixed(self,amount=None,pair=None,withdrawal=None,returnAddress=None,destTag=None,rsAddress=None,apiKey=None):
		"""
		Same as shapeshift_shift_request(...input...) but using a fixed amount

		@input:
			* - 1st scenario:
			amount = the amount to be sent to the withdrawal address
			withdrawal = the address for coin to be sent to
			pair = what coins are being exchanged in the form [input coin]_[output coin]  ie ltc_btc
			returnAddress = (Optional) address to return deposit to if anything goes wrong with exchange
			destTag = (Optional) Destination tag that you want appended to a Ripple payment to you
			rsAddress = (Optional) For new NXT accounts to be funded, supply this on NXT payment to you
			apiKey = (Optional) Your affiliate PUBLIC KEY, for volume tracking, affiliate payments, split-shifts, etc...

			* - 2nd scenario: inputs are only: amount and pair:
				Note :  This request will only return information about a quoted rate
				        This request will NOT generate the deposit address.

		"""
		__url = self.url_post_exchange_fixed

		if amount != None and pair != None and withdrawal != None:
			__post_data = {"amount":amount, "pair": pair.upper(), "withdrawal": withdrawal, "returnAddress": returnAddress,
			"apiKey": apiKey, "destTag": destTag, "rsAddress": rsAddress}

			return self.post_exchange(url = __url, post_data = __post_data)

		elif withdrawal == None:
			__post_data = {"amount": amount, "pair": pair.upper()}

			return self.post_exchange(__url, post_data = __post_data)
		else:
			print("Usage: ShapeShiftAPI.shapeshift_shift_request_fixed(... inputs ...) ")
			print("inputs:")
			print("\t amount = 'Your amount' (Required)")
			print("\t pair = 'Your pair' (Required)")
			print("\t withdrawal = 'Your withdrawal address' (Required)")
			print("\t returnAddress = 'Your return address' (Optional)")
			print("\t destTag = 'Your Ripple destTag' (Optinal)")
			print("\t rsAddress = 'Your rsAddress for NXT new accounts' (Optinal)")
			print("\t apiKey = 'Your ShapeShift APIKEY' (optional)")
			return None

	def shapeshift_request_mail(self, mail = None, txid = None):
		"""
		@input:
			mail : Reception email
			txid : ShapeShift transaction ID

		@return (if success):
			{"email":{"status":"success", "message":"Email receipt sent"}}
		@return (if failure): None
		"""
		__url = self.url_request_mail
		if mail != None and txid != None:
			__post_data = {"email": mail, "txid": txid}

			return self.post_exchange(url = __url, post_data = __post_data)

		else:
			print("Usage: ShapeShiftAPI.shapeshift_request_mail(mail = 'Recip email', txid = 'Transaction ID')")
			return None

	def post_exchange(self, url = None, post_data = None):
		"""
			Communication with ShapeShift server through POST and GET
		"""
		try:
			json_data = dumps(post_data).encode("UTF8")
			request = Request(url, json_data, headers = {'Content-Type': 'application/json'})
			response = urlopen(request)
			content = response.read()
			data = loads(content.decode("UTF8"))
			return data

		except Exception as err:
			print("Error", err)
			return None

	def shapeshift_shift_request(self,pair=None,withdrawal=None,returnAddress=None,destTag=None,rsAddress=None,apiKey=None):
		"""
		@input:
			pair : (Required) What coins are being exchanged in the form [input coin]_[output coin]  ie btc_ltc
			withdrawal : (Required) The address for resulting coin to be sent to
			returnAddress : (Optional) Address to return deposit to if anything goes wrong with exchange
			destTag : (Optional) Destination tag that you want appended to a Ripple payment to you
			rsAddress : (Optional) For new NXT accounts to be funded, you supply this on NXT payment to you
			apiKey : (Optional) Your affiliate PUBLIC KEY, for volume tracking, affiliate payments, split-shifts, etc...

		@return (if success) example for the pair 'btc_eth': type = dict :
		{'withdrawal': '0xea674fdde714fd979de3edf0f56aa9716b898ec8', 'depositType': 'BTC',
		 'public': None, 'orderId': '69116c9a-9e60-4dd6-aeed-22dfa0891bd4',
		  'withdrawalType': 'ETH', 'deposit': '15joRVhXifqVoe8v7k4cX7o4L3L3MTrbkP', 'apiPubKey': 'shapeshift'}
		 @return (if failure): None
		"""
		__url = self.url_post_exchange
		if pair != None and withdrawal != None:
			__post_data = {"pair": pair.upper(), "withdrawal": withdrawal, "returnAddress": returnAddress,
			"apiKey": apiKey, "destTag": destTag, "rsAddress": rsAddress}

			return self.post_exchange(url = __url, post_data = __post_data)
		else:
			print("Usage: ShapeShiftAPI.shapeshift_shift_request(... inputs ...) ")
			print("inputs:")
			print("\t pair = 'Your pair' (Required)")
			print("\t withdrawal = 'Your withdrawal address' (Required)")
			print("\t returnAddress = 'Your return address' (Optional)")
			print("\t destTag = 'Your Ripple destTag' (Optinal)")
			print("\t rsAddress = 'Your rsAddress for NXT new accounts' (Optinal)")
			print("\t apiKey = 'Your ShapeShift APIKEY' (optional)")
			return None


	def check_address(self, address = None, coin = None):
		"""
		if address != None and coin != None:
			return bool (True or False) : True = valid address and/or coin / False = invalid address and/or coin
		else:
			return None : Check usage
		"""
		__url = self.url_valid_address
		if address != None and coin != None:
			__url += address+"/"+coin.upper()
			return self.load_url(__url)["isvalid"]
		else:
			print("Usage: ShapeShiftAPI.check_adress(adresses = 'Your coin adresse', coin='Your coin symbol')")
			return None

	def return_shapeshift_coins(self, only_symbol = False):
		"""
		if only_symbol == False:
			return all ShapeShift's supported coins with their name, symbol, etc.. (1)
		else:
			return only ShapeShift's supported coins symbols (2)

		@return(1): dict of dicts {'coinx':{...}, ..., 'coiny':{...}} example:
		{'VOX': {'status': 'available', 'symbol': 'VOX', 'name': 'Voxels',
		 'image': 'https://shapeshift.io/images/coins/voxels.png'},
		 ...
		  'LSK': {'status': 'available', 'symbol': 'LSK', 'name': 'Lisk',
		   'image': 'https://shapeshift.io/images/coins/lisk.png'}}

		@return2: tuple [...] example:
		['SC', 'OMNI', ...,  'DGD', 'SDC', 'NXT']

		"""
		__url = self.url_coins
		if only_symbol == False:
			return self.load_url(__url)
		else:
			return [x for x in self.load_url(__url)]

	def return_shapeshift_market(self, pair = None):
		"""
		if pair == None:
			return all ShapeShift's supported coins market (1)
		else:
			return only ShapeShift's supported coin market (2)

		@return(1): tuple of dicts [{...}, ..., {...}] example:
		[{'limit': 198.58387989, 'minerFee': 0.01, 'min': 0.01071429, 'rate': '1.62633730', 'maxLimit': 198.58387989,
		 'pair': 'NVC_PPC'},
		 ....
		 {'limit': 198.58387989, 'minerFee': 0.005, 'min': 0.005, 'rate': '1.73659745', 'maxLimit': 198.58387989,
		  'pair': 'NVC_NMC'}]

		@return(2): dict {...} example:
		{'pair': 'BTC_ETH', 'minimum': 0.00041854, 'limit': 1.52842099, 'minerFee': 0.01, 'maxLimit': 3.05684198,
		 'rate': 47.60484755}

		"""
		__url = ""
		if pair == None:
			__url = self.url_market
		else:
			__url = self.url_market+pair.upper()

		return self.load_url(__url)

	def return_pair_limit(self, pair = None):
		"""
		return ShapeShift's pair limits

		@return: dict {...} example for the pair 'btc_eth' :
		{'min': '0.00041636', 'pair': 'btc_eth', 'limit': '1.53243788'}
		"""
		if pair != None:
			__url = self.url_limit+pair.upper()
			return self.load_url(__url)
		else:
			print("Please provide a valid pair!\n-> use: ShapeShiftAPI.return_pair_limit(pair='coin1_coin2')")
			return []

	def return_shapeshift_pairs_info(self):
		"""
		return all supported ShapeShift's pairs informations

		@return: list of dicts [{...}, ..., {...}] example:
		[{'pair': 'NMC_NVC', 'rate': '0.49737499', 'min': 0.00349153, 'minerFee': 0.001,
		 'maxLimit': 69.361676, 'limit': 69.361676},
		 ........
		  {'pair': 'NVC_NMC', 'rate': '1.73659745', 'min': 0.005, 'minerFee': 0.005,
		   'maxLimit': 198.58387989, 'limit': 198.58387989}]
		"""
		__url = self.url_rate
		return self.load_url(__url)

	def load_url(self, url):
		"""
		return JSON decoded data
		"""
		try:
			__response = urlopen(url)
			__content = __response.read()
			data = loads(__content.decode("UTF8"))
			return data
		except Exception:
			print("Cannot retrieve data from: ", url)
			return []
