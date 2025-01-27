import cv2
import os

kamera = cv2.VideoCapture(0)  # Gunakan '0' untuk kamera default
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = kamera.read()  # Pisahkan 'ret' dan 'frame'
    if not ret:  # Jika frame tidak berhasil dibaca
        print("Gagal membaca frame")
        break

    # Ubah frame menjadi model warna HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape  # Ambil ukuran frame

    # Tentukan posisi tengah
    cx = int(width / 2)
    cy = int(height / 2)

    # Gambar lingkaran di tengah frame
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), -1)

    # Ambil nilai pixel dari channel HSV di tengah frame
    pixsel_center = hsv_frame[cy, cx]
    hue = pixsel_center[0]
    saturation = pixsel_center[1]
    value = pixsel_center[2]

    color = "tidak terdeteksi"
    color_rgb = (0, 0, 0)

    if value < 50:
        color = "Hitam"
        color_rgb = (0, 0, 0)
    elif saturation < 50:
        color = "Putih"
        color_rgb = (255, 255, 255)
    elif hue < 10 or hue > 160:
        color = "Merah"
        color_rgb = (0, 0, 255)
    
    os.system("cls")
    
    print(f"Hue: {hue}, Saturation: {saturation}, Value: {value}, Deteksi: {color}")
    
    # Menampilkan teks dengan warna yang sesuai
    cv2.putText(frame, color, (cx - 100, cy - 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color_rgb, 2)   
    
    # Tampilkan hasil di window
    cv2.imshow("Program pengenalan warna", frame)

    key = cv2.waitKey(1)
    if key == ord("k"):  # Tekan 'k' untuk keluar
        break

kamera.release()
cv2.destroyAllWindows()
