import pyqrcode
url ='https://youtube.com/channel/UC2MSiYXij4jBeEsSv5bz16g'
k=pyqrcode.create(url)
k.svg('qr.svg',scale=10)
