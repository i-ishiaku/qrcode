import qrcode as qr
import image
# a variable to take user input
data = input("Please leave a message: ")
# output file name
filename = "message.png"
# generate qr code
img = qr.make(data)
# save img to a file
img.save(filename)
