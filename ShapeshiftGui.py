#!/usr/bin/python3

from gi.repository import Gtk, GLib, GObject, GdkPixbuf
from os import listdir
from random import randint
from src.GetCoinSymbol import GetCoinSymbol
from src.GetPairMarket import GetPairMarket
from src.ValidateAddress import ValidateAddress
from src.PostExchange import PostExchange
from threading import Thread

class ShapeshiftGui(object):
    """
    """
    def __init__(self):
        """
            initialize the app
        """
        # Initialize GetCoinSymbol class
        GetCoinSymbol.__init__(self)
        self.GetCoinSymbol = GetCoinSymbol()

        # Initialize GetPairMarket class
        GetPairMarket.__init__(self)
        self.GetPairMarket = GetPairMarket()

        # Initialize ValidateAddress class
        ValidateAddress.__init__(self)
        self.ValidateAddress = ValidateAddress()

        # Initialize PostExchange class
        PostExchange.__init__(self)
        self.PostExchange = PostExchange()

        # Build ui from xml file
        self.builder = Gtk.Builder()
        self.builder.add_from_file("ui/shapeshift_ui.glade")

        # Cell + imgs

        box = self.builder.get_object("box2")

        self.coin_list = ["bitcoin", "bitCrystals", "bitshares", "blackcoin", "clams",
        "counterparty", "dash", "digibyte", "digixDao", "dogecoin", "emercoin",
        "ether", "ether Classic", "factoids", "lisk", "litecoin", "maidsafe",
        "mastercoin", "mintcoin", "monacoin", "monero", "namecoin", "novacoin",
        "nubits", "nxt", "peercoin", "reddcoin", "shadowcash", "siacoin", "storjX",
        "theDao", "vertcoin", "voxels", "steem", "tether", "vericoin", "LBRY Credits" ]

        func_coin = lambda x: GdkPixbuf.Pixbuf.new_from_file_at_size(x , 50, 50)

        # Create a Gtk.ComboBox with images
        # 1st ComboBox
        store = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        for i in self.coin_list:
            store.append([i, func_coin("img/"+i+".png")])

        self.combo = Gtk.ComboBox.new_with_model(store)
        renderer = Gtk.CellRendererText()
        self.combo.pack_start(renderer, True)
        self.combo.add_attribute(renderer, "text", 0)

        renderer = Gtk.CellRendererPixbuf()
        self.combo.pack_start(renderer, False)
        self.combo.add_attribute(renderer, "pixbuf", 1)

        self.combo.connect("changed", self.get_new_values)

        # Connect to a signal : Get new informations when the active id change
        box.pack_start(self.combo, False, False, False)

        # Here you can add Gtk.Image to GUI
        # ---- Here ----

        # 2nd ComboBox
        store2 = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        for i in self.coin_list:
            store2.append([i, func_coin("img/"+i+".png")])

        self.combo2 = Gtk.ComboBox.new_with_model(store2)
        renderer = Gtk.CellRendererText()
        self.combo2.pack_start(renderer, True)
        self.combo2.add_attribute(renderer, "text", 0)

        renderer = Gtk.CellRendererPixbuf()
        self.combo2.pack_start(renderer, False)
        self.combo2.add_attribute(renderer, "pixbuf", 1)

        # Connect to a signal : Get new informations when the active id change
        self.combo2.connect("changed", self.get_new_values)

        box.pack_end(self.combo2, False, False, False)

        self.img_name1, self.img_name2 = None, None

        # Initialize labels
        self.pair_value = self.builder.get_object("label11")
        self.rate_value = self.builder.get_object("label12")
        self.miner_fees_value = self.builder.get_object("label13")
        self.exch_limit_value = self.builder.get_object("label14")
        self.min_exch_value = self.builder.get_object("label15")
        self.available_value = self.builder.get_object("label16")
        self.validation_value = self.builder.get_object("label17")

        # Initialize address entry & refund entry
        self.address_entry = self.builder.get_object("entry1")
        self.refund_entry = self.builder.get_object("entry2")

        # Initialize transaction labels & entries
        self.expander = self.builder.get_object("expander1")
        self.deposit_type_label = self.builder.get_object("label3")
        self.withdrawl_type_label = self.builder.get_object("label22")
        self.deposit_address_entry = self.builder.get_object("entry3")
        self.withdrawal_address_entry = self.builder.get_object("entry4")
        self.order_id_entry = self.builder.get_object("entry5")

        # Test
        echange = self.builder.get_object("button1")
        echange.connect("clicked", self.run_exchange)
        self.coin1, self.coin2 = None, None

        # Run default
        #self.set_default_buttons_img()

    def get_exchange_info(self):
        """
            Run TrasactionGui
        """
        validation = False

        address = self.address_entry.get_text()
        address = address.replace(" ", "")

        try:
            validation = self.ValidateAddress.validate(address = address, coin = self.coin2)
            if validation:
                pair = self.coin1+"_"+self.coin2
                exchange_info = self.PostExchange.exchange(p = pair, w = address)
                print("exchange_info: ", exchange_info)

                pair_coins = self.coin1+"/"+self.coin2
                deposit_type = exchange_info["depositType"]
                withdrawl_type = exchange_info["withdrawalType"]
                deposit_address = exchange_info["deposit"]
                withdrawal_address = exchange_info["withdrawal"]
                order_id = exchange_info["orderId"]

                # DEBUG
                print(
                "\t\tPair: {0}\n\
                Deposit type: {1}\n\
                Deposit address: {2}\n\
                Withdrawal type: {3}\n\
                Withdrawal address: {4}\n\
                Order ID: {5}".format(pair_coins, deposit_type, deposit_address, withdrawl_type, withdrawal_address, order_id)
                )

                self.deposit_type_label.set_markup("<b>"+deposit_type+"</b>")
                self.withdrawl_type_label.set_marjup("<b>"+withdrawl_type+"</b>")
                self.deposit_address_entry.set_text(deposit_address)
                self.withdrawal_address_entry.set_text(withdrawal_address)
                self.order_id_entry.set_text(order_id)



        except Exception as e:
            print("get_exchange_info: Error: ", e)
            validation = False

        print("validation: ", validation)
        if not validation:
            self.address_entry.set_text("Enter a valid {0} address".format(self.coin2))


    def run_exchange(self, widget):
        """
        """
        thread = Thread(target = self.get_exchange_info)
        thread.daemon = True
        thread.start()

        # DEBUG
        print("Thread exchange ID: ", thread.ident)
        print("Thread alive: ", thread.isAlive())


    def get_new_values(self, widget):
        """
            When ComboBox changed, main window will update all labels informations
        """
        nb1, nb2 = self.combo.get_active(), self.combo2.get_active()
        self.img_name1, self.img_name2 = self.coin_list[nb1], self.coin_list[nb2]
        self.get_items(widget = "window")


    def update_gui_info(self):
        """
        """
        self.pair_value.set_markup("<i>Retrieving...</i>")
        self.rate_value.set_markup("<i>Retrieving...</i>")
        self.miner_fees_value.set_markup("<i>Retrieving...</i>")
        self.exch_limit_value.set_markup("<i>Retrieving...</i>")
        self.min_exch_value.set_markup("<i>Retrieving...</i>")
        self.available_value.set_markup("<i>Retrieving...</i>")
        self.validation_value.set_markup('<b><span foreground="red">Not valid</span></b>')
        self.address_entry.set_text("")
        self.refund_entry.set_text("")

        coin1 = self.GetCoinSymbol.get_symbol_of_coin(coin = self.img_name1)
        coin2 = self.GetCoinSymbol.get_symbol_of_coin(coin = self.img_name2)

        if coin1 != None and coin2 != None:

            try:
                pair_market = self.GetPairMarket.get_pair_market_info(pair = coin1+"_"+coin2)

                self.pair_value.set_markup("<b>{0}/{1}</b>".format(coin1, coin2))
                self.rate_value.set_markup("<b>"+str(pair_market["rate"])+"</b>")
                self.miner_fees_value.set_markup("<b>"+str(pair_market["minerFee"])+"</b>")
                self.exch_limit_value.set_markup("<b>"+str(pair_market["limit"])+"</b>")
                self.min_exch_value.set_markup("<b>"+str(pair_market["minimum"])+"</b>")
                self.available_value.set_markup("<b>"+str(pair_market["maxLimit"])+"</b>")
                self.validation_value.set_markup('<b><span foreground="green">Valid</span></b>')
                self.address_entry.set_text('Enter your "{0}" address'.format(coin2))
                self.refund_entry.set_text('Enter your "{0}" address'.format(coin1))
                self.coin1, self.coin2 = coin1, coin2
            except Exception as e:
                # DEBUG
                print("update_gui_info: Error", e)

                self.rate_value.set_text(" - ")
                self.miner_fees_value.set_text(" - ")
                self.exch_limit_value.set_text(" - ")
                self.miner_fees_value.set_text(" - ")
                self.min_exch_value.set_text(" - ")
                self.available_value.set_text(" - ")
                self.validation_value.set_markup('<b><span foreground="red">Not valid</span></b>')
                pass

        else:
            self.pair_value.set_markup('<span foreground="red">-/- (Pair not accepted)</span>')
            self.rate_value.set_text(" - ")
            self.miner_fees_value.set_text(" - ")
            self.exch_limit_value.set_text(" - ")
            self.miner_fees_value.set_text(" - ")
            self.min_exch_value.set_text(" - ")
            self.available_value.set_text(" - ")
            self.validation_value.set_markup('<b><span foreground="red">Not valid</span></b>')

        # DEBUG
        print("update_gui_info: {0} - {1}".format(self.img_name1, self.img_name2))

    def get_items(self, widget):
        """
            Threading update_gui_info to prevent freezing GUI
        """
        thread = Thread(target = self.update_gui_info)
        thread.daemon = True
        thread.start()
        # Debug
        print("Thread get_items ID: ", thread.ident)

    def set_default_buttons_img(self):
        """
            Set random ComboBox coins
        """
        nb1, nb2 = None, None

        while True:
            nb1 = randint(0, len(self.coin_list)-1)
            nb2 = randint(0, len(self.coin_list)-1)
            if nb1 != nb2:
                # DEBUG
                #print(nb1, nb2, len(self.list_imgs_path))
                break

        self.combo.set_active(nb1)
        self.combo2.set_active(nb2)
        self.img_name1, self.img_name2 = self.coin_list[nb1], self.coin_list[nb2]

    def main(self):
        """
            Main function
        """
        window = self.builder.get_object("window1")
        window.connect("delete-event", self.safe_quit, "kill ui")
        window.show_all()

    def safe_quit(self, widget, args, msg):
        """
            Kill the current widget
        """
        # DEBUG
        #print("Safe exit ...", widget, args, msg)
        Gtk.main_quit()


if __name__ == '__main__':
    GObject.threads_init()
    app = ShapeshiftGui()
    app.set_default_buttons_img()
    #while Gtk.events_pending():
        #Gtk.main_iteration_do(block = False)
    app.main()
    #app.update_gui_info()
    Gtk.main()
