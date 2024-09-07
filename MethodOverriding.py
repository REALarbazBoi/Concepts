class iphone6:

    def home(self):
        print("Home butter is pressed")

class iphoneX(iphone6):

    def home(self):
        print("home is touched")
        super().home()

i6 = iphone6()
i6.home()

ix = iphoneX()
ix.home()