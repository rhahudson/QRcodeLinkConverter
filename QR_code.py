import png
import pyqrcode
import time



link = input("Enter Website: ")
name = input("Enter Desired Name of File (PNG Format): ")
start_time = time.time()
url = pyqrcode.create(link)
url.png(f"{name}.png", scale=12)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Successfully Created QR Code in {elapsed_time:.5f} seconds")