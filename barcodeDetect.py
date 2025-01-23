import cv2 as cv
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
# adsfads;fklasjdf;klajsdf;lkasjf;lksdajfsda;lkfdjasd;lfksajd;
def barcodeDetect(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    barcodes = decode(gray)

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        print("Barcode Data: ", barcode_data)
        print("Barcode Type: ", barcode_type)

        (x, y, w, h) = barcode.rect
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        cv.putText(image, f"{barcode_data} ({barcode_type})", (x, y - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    plt.imshow(imageRGB)
    plt.axis("off")
    plt.show()

image = cv.imread("/home/chogene/openCV/projects/example_barcodes/pocariBacode.jpg")

barcodeDetect(image)
