import qrcode

text = "Pavlo Dranytskyi, IT-21, pavlodranitskiy@gmail.com"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")
print(f"QR data: {text}")
