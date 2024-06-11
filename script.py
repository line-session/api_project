import cv2
from pyzbar import pyzbar
import requests
import numpy as np
import webbrowser
import time
def decode(frame):
    decoded_objects = pyzbar.decode(frame)
    qr_detected = False  # Flag to track QR code detection
    for obj in decoded_objects:
        if not qr_detected:
            cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
                        (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
                        (0, 255, 0), 2)
            text = f"{obj.type}: {obj.data.decode('utf-8')}"
            cv2.putText(frame, text, (obj.rect.left, obj.rect.top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print("Detected barcode:", text)
            display_user(obj.data.decode('utf-8'), frame)
            qr_detected = True  # Set flag to True once QR code is detected
    return frame, qr_detected

def display_user(code_barre, frame):
    try:
        response = requests.post('http://127.0.0.1:8000/api/etudiant/enregistrer-log/', data={'code_barre': code_barre})
        if response.status_code == 200:
            user = response.json()
            nom_user = user['nom']
            image_path = user['photo']
            print("Bonjour:", nom_user)
            url_path = f"http://127.0.0.1:8000{image_path}"
            webbrowser.open(url_path)
            time.sleep(2)  # Sleep for 2 seconds after displaying user information
        else:
            print(f"User not found for barcode: {code_barre}. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error accessing the API: {e}")
    
def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la webcam")
        return

    qr_detected = False  # Flag to track if QR code has been detected
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not qr_detected:
            frame, qr_detected = decode(frame)
            cv2.imshow('Barcode/QR code reader', frame)
        else:
            # Pause for 3 seconds after detecting QR code
            time.sleep(3)
            qr_detected = False  # Reset flag to detect new QR codes

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
