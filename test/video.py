
# Importing library
import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        detectedBarcodes = decode(frame)
      
    # If not detected then print the message
        if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!")
        else:
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes: 
                # Locate the barcode position in image
                (x, y, w, h) = barcode.rect
                
                # Put the rectangle in image using cv2 to highlight the barcode
                cv2.rectangle(frame, (x - 10, y - 10),
                            (x + w + 10, y + h + 10),
                            (255, 0, 0), 2)
                
                if barcode.data != "":
                
                # Print the barcode data
                    print(barcode.data)
                    print(barcode.type)
                    
        #Display the image
        cv2.imshow("Image", frame)
        
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
