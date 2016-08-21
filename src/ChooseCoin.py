#!/usr/bin python3
from gi.repository import Gtk

class ChooseCoin(Gtk.Window):
    """
    """
    def __init__(self):
        """
        """
        builder = Gtk.Builder()
        builder.add_from_file("ui/choose_ui.glade")
        self.window = builder.get_object("window1")
        # button1
        b1 = builder.get_object("button1")
        img = Gtk.Image.new_from_file("img/bitcoin.png")
        b1.set_image(img)
        b1.set_label("bitcoin")
        b1.connect("clicked", ChooseCoin.return_new_coin, b1)

        # button2
        b2 = builder.get_object("button2")
        img = Gtk.Image.new_from_file("img/bitCrystals.png")
        b2.set_image(img)
        b2.set_label("bitCrystals")
        b2.connect("clicked", ChooseCoin.return_new_coin, b2)

        # button3
        b3 = builder.get_object("button3")
        img = Gtk.Image.new_from_file("img/bitshares.png")
        b3.set_image(img)
        b3.set_label("bitshares")
        b3.connect("clicked", ChooseCoin.return_new_coin, b3)

        # button4
        b4 = builder.get_object("button4")
        img = Gtk.Image.new_from_file("img/blackcoin.png")
        b4.set_image(img)
        b4.set_label("blackcoin")
        b4.connect("clicked", ChooseCoin.return_new_coin, b4)

        # button5
        b5 = builder.get_object("button5")
        img = Gtk.Image.new_from_file("img/clams.png")
        b5.set_image(img)
        b5.set_label("clams")
        b5.connect("clicked", ChooseCoin.return_new_coin, b5)

        # button6
        b6 = builder.get_object("button6")
        img = Gtk.Image.new_from_file("img/counterparty.png")
        b6.set_image(img)
        b6.set_label("counterparty")
        b6.connect("clicked", ChooseCoin.return_new_coin, b6)

        # button7
        b7 = builder.get_object("button7")
        img = Gtk.Image.new_from_file("img/dash.png")
        b7.set_image(img)
        b7.set_label("dash")
        b7.connect("clicked", ChooseCoin.return_new_coin, b7)

        # button8
        b8 = builder.get_object("button8")
        img = Gtk.Image.new_from_file("img/digibyte.png")
        b8.set_image(img)
        b8.set_label("digibyte")
        b8.connect("clicked", ChooseCoin.return_new_coin, b8)

        # button9
        b9 = builder.get_object("button9")
        img = Gtk.Image.new_from_file("img/digixDao.png")
        b9.set_image(img)
        b9.set_label("digixDao")
        b9.connect("clicked", ChooseCoin.return_new_coin, b9)

        # button10
        b10 = builder.get_object("button10")
        img = Gtk.Image.new_from_file("img/dogecoin.png")
        b10.set_image(img)
        b10.set_label("dogecoin")
        b10.connect("clicked", ChooseCoin.return_new_coin, b10)

        # button11
        b11 = builder.get_object("button11")
        img = Gtk.Image.new_from_file("img/emercoin.png")
        b11.set_image(img)
        b11.set_label("emercoin")
        b11.connect("clicked", ChooseCoin.return_new_coin, b11)

        # button12
        b12 = builder.get_object("button12")
        img = Gtk.Image.new_from_file("img/ether.png")
        b12.set_image(img)
        b12.set_label("ether")
        b12.connect("clicked", ChooseCoin.return_new_coin, b12)

        # button13
        b13 = builder.get_object("button13")
        img = Gtk.Image.new_from_file("img/ether Classic.png")
        b13.set_image(img)
        b13.set_label("ether Classic")
        b13.connect("clicked", ChooseCoin.return_new_coin, b13)

        # button14
        b14 = builder.get_object("button14")
        img = Gtk.Image.new_from_file("img/factoids.png")
        b14.set_image(img)
        b14.set_label("factoids")
        b14.connect("clicked", ChooseCoin.return_new_coin, b14)

        # button15
        b15 = builder.get_object("button15")
        img = Gtk.Image.new_from_file("img/lisk.png")
        b15.set_image(img)
        b15.set_label("lisk")
        b15.connect("clicked", ChooseCoin.return_new_coin, b15)

        # button16
        b16 = builder.get_object("button16")
        img = Gtk.Image.new_from_file("img/litecoin.png")
        b16.set_image(img)
        b16.set_label("litecoin")
        b16.connect("clicked", ChooseCoin.return_new_coin, b16)

        # button17
        b17 = builder.get_object("button17")
        img = Gtk.Image.new_from_file("img/maidsafe.png")
        b17.set_image(img)
        b17.set_label("maidsafe")
        b17.connect("clicked", ChooseCoin.return_new_coin, b17)

        # button18
        b18 = builder.get_object("button18")
        img = Gtk.Image.new_from_file("img/mastercoin.png")
        b18.set_image(img)
        b18.set_label("mastercoin")
        b18.connect("clicked", ChooseCoin.return_new_coin, b15)

        # button19
        b19 = builder.get_object("button19")
        img = Gtk.Image.new_from_file("img/mintcoin.png")
        b19.set_image(img)
        b19.set_label("mintcoin")
        b19.connect("clicked", ChooseCoin.return_new_coin, b19)

        # button20
        b20 = builder.get_object("button20")
        img = Gtk.Image.new_from_file("img/monacoin.png")
        b20.set_image(img)
        b20.set_label("monacoin")
        b20.connect("clicked", ChooseCoin.return_new_coin, b20)

        # button21
        b21 = builder.get_object("button21")
        img = Gtk.Image.new_from_file("img/monero.png")
        b21.set_image(img)
        b21.set_label("monero")
        b21.connect("clicked", ChooseCoin.return_new_coin, b21)

        # button22
        b22 = builder.get_object("button22")
        img = Gtk.Image.new_from_file("img/namecoin.png")
        b22.set_image(img)
        b22.set_label("namecoin")
        b22.connect("clicked", ChooseCoin.return_new_coin, b22)

        # button23
        b23 = builder.get_object("button23")
        img = Gtk.Image.new_from_file("img/novacoin.png")
        b23.set_image(img)
        b23.set_label("novacoin")
        b23.connect("clicked", ChooseCoin.return_new_coin, b23)

        # button24
        b24 = builder.get_object("button24")
        img = Gtk.Image.new_from_file("img/nubits.png")
        b24.set_image(img)
        b24.set_label("nubits")
        b24.connect("clicked", ChooseCoin.return_new_coin, b24)

        # button25
        b25 = builder.get_object("button25")
        img = Gtk.Image.new_from_file("img/nxt.png")
        b25.set_image(img)
        b25.set_label("nxt")
        b25.connect("clicked", ChooseCoin.return_new_coin, b25)

        # button26
        b26 = builder.get_object("button26")
        img = Gtk.Image.new_from_file("img/peercoin.png")
        b26.set_image(img)
        b26.set_label("peercoin")
        b26.connect("clicked", ChooseCoin.return_new_coin, b26)

        # button27
        b27 = builder.get_object("button27")
        img = Gtk.Image.new_from_file("img/reddcoin.png")
        b27.set_image(img)
        b27.set_label("reddcoin")
        b27.connect("clicked", ChooseCoin.return_new_coin, b27)

        # button28
        b28 = builder.get_object("button28")
        img = Gtk.Image.new_from_file("img/shadowcash.png")
        b28.set_image(img)
        b28.set_label("shadowcash")
        b28.connect("clicked", ChooseCoin.return_new_coin, b28)

        # button29
        b29 = builder.get_object("button29")
        img = Gtk.Image.new_from_file("img/siacoin.png")
        b29.set_image(img)
        b29.set_label("siacoin")
        b29.connect("clicked", ChooseCoin.return_new_coin, b29)

        # button30
        b30 = builder.get_object("button30")
        img = Gtk.Image.new_from_file("img/storjX.png")
        b30.set_image(img)
        b30.set_label("storjX")
        b30.connect("clicked", ChooseCoin.return_new_coin, b30)

        # button31
        b31 = builder.get_object("button31")
        img = Gtk.Image.new_from_file("img/theDao.png")
        b31.set_image(img)
        b31.set_label("theDao")
        b31.connect("clicked", ChooseCoin.return_new_coin, b31)

        # button32
        b32 = builder.get_object("button32")
        img = Gtk.Image.new_from_file("img/vertcoin.png")
        b32.set_image(img)
        b32.set_label("vertcoin")
        b32.connect("clicked", ChooseCoin.return_new_coin, b32)

        # button33
        b33 = builder.get_object("button33")
        img = Gtk.Image.new_from_file("img/voxels.png")
        b33.set_image(img)
        b33.set_label("voxels")
        b33.connect("clicked", ChooseCoin.return_new_coin, b33)

        self.returned_coin = None
        ChooseCoin.button_n = None


    def return_new_coin(self, widget):
        """
        """
        # DEBUG
        try:
            print("img/"+widget.get_label()+".png")
            self.returned_coin = "img/"+widget.get_label()+".png"

        except TypeError as e:
            print("Can't print widget label")

    def set_new_image(self, widget, args):
        """
        """
        ChooseCoin.button_n = args


    def main(self):
        """
        """
        self.window.connect("destroy", self.safe_destroy)
        self.window.show_all()

    def safe_destroy(self, widget):
        """
        """
        print("widget to destroy: ", widget)
        self.window.destroy()
