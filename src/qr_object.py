import qrcode

class QRObject(qrcode.QRCode):
    
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.data = None
        self.bg_color = 'white'
        self.fill_color = 'black'

    #Setters
    def set_data(self,data):
        hayData = False
        if data:
            self.data = data
            self.qr.add_data(data)
            self.qr.make(fit=True)
            hayData = True
        return hayData
       
    def set_bg_color(self,new_color):
        self.bg_color = new_color
    
    def set_fill_color(self,new_color):
        self.fill_color = new_color
    
    #Getters
    def get_qr(self):
        img = self.qr.make_image(fill = self.fill_color, back_color = self.bg_color)
        return img

