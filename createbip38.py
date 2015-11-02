__author__ = 'pete'
from bip38 import *
from bitcoin import *
from qrcode import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

print 'BIP38 generator from pass phrase and supplied private or random key. Generates bip38-QR.jpg..'
print 'Enter passphrase:'
pasw = raw_input()
if not pasw:
    print 'you must enter a passkey!'
    exit()
print 'Type or paste private key: (if you hit enter a random key will be generated)'
txt = raw_input()
if not txt:
    print 'Using randomly generated private key..'
    priv = random_key()
else:
    priv = txt
priv2 = decode_privkey(priv,'hex')
wif = encode_privkey(priv, 'wif')

addr = privtoaddr(priv)
bip = bip38_encrypt(priv,pasw)
bipp = bip38_decrypt(bip,pasw)
bina = decode_privkey(bipp,'wif')
hexa = encode_privkey(bina, 'hex')
print 'Bitcoin private key (hex)'
print priv
print 'Bitcoin private key (raw)'
print priv2
print 'Bitcoin private key (WIF)'
print wif
print " "
print 'BIP38 address:'
print bip
print 'for bitcoin address:'
print privtoaddr(priv)
print " "
print 'Error checking..should match above..'
print hexa
print bina
print bipp
print 'and passcode:'
print pasw



qr = QRCode(box_size=8, border=3,error_correction=ERROR_CORRECT_Q)
qr.add_data(bip)
im = qr.make_image()
im_w, im_h = im.size

qr2 = QRCode(box_size=8, border=3,error_correction=ERROR_CORRECT_M)     #create a 2nd instance to play with sizes..
qr2.add_data(addr)
im2 = qr2.make_image()
im2_w, im2_h = im2.size

img = Image.open("star_field.jpg")              #background of paper wallet
img_w, img_h = img.size

over_w = img_w - (im2_w+im_w)
offs = over_w / 4

offset = ((img_w /2) - im_w, (img_h - im_h) / 2)
offset2 = (580, 130)

img.paste(im, offset)   #paste the QR's into the background image..
img.paste(im2,offset2)

draw = ImageDraw.Draw(img)
#font = ImageFont.truetype("Times New Roman.ttf",14)                        #print text above and below the QR's..
font = ImageFont.truetype("Arial Bold.ttf",22)
draw.text((offs, 20), 'BIP38:  '+ bip, (255,255,255),font)
draw.text((((img_w - im_w) / 2),(img_h - 40)),'Address:  '+ addr,(255,255,255),font)

img.save('bip38-QR.jpg')
