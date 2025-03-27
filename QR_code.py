"""import qrcode as qr
img= qr.make("https://www.facebook.com/share/1CBPxfGbFb/?mibextid=wwXIfr")
img.save("My_facebook_account_link.png")"""

import qrcode
from PIL import Image
from qrcode.console_scripts import error_correction

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.facebook.com/share/1CBPxfGbFb/?mibextid=wwXIfr")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("My_facebook_account_link.png")