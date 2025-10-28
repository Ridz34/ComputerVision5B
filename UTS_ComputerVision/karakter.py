import cv2
import numpy as np
import os

# Pastikan folder output ada
os.makedirs("output", exist_ok=True)

# 1. Membuat kanvas hitam 400x400
canvas = np.full((400, 400, 3), (0, 0, 0), dtype=np.uint8)

# Gambar karakter sederhana: robot wajah
cv2.rectangle(canvas, (120, 100), (280, 260), (100, 255, 255), -1)  # kepala
cv2.circle(canvas, (160, 160), 20, (0, 0, 0), -1)  # mata kiri
cv2.circle(canvas, (240, 160), 20, (0, 0, 0), -1)  # mata kanan
cv2.rectangle(canvas, (150, 210), (250, 230), (0, 0, 0), -1)  # mulut
cv2.rectangle(canvas, (180, 60), (220, 100), (150, 255, 150), -1)  # antena
cv2.circle(canvas, (200, 60), 10, (0, 0, 255), -1)  # ujung antena
cv2.putText(canvas, "ROBO", (150, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imwrite("output/karakter.png", canvas)

# 2. Transformasi

# a. Translasi
M_trans = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(canvas, M_trans, (400, 400))
cv2.imwrite("output/translate.png", translated)

# b. Rotasi
center = (200, 200)
M_rot = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated = cv2.warpAffine(canvas, M_rot, (400, 400))
cv2.imwrite("output/rotate.png", rotated)

# c. Resize
resized = cv2.resize(canvas, (200, 200))
cv2.imwrite("output/resize.png", resized)

# d. Crop
cropped = canvas[100:300, 120:320]
cv2.imwrite("output/crop.png", cropped)

# 3. Operasi Bitwise dan Aritmatika
background = np.full((400, 400, 3), (50, 100, 150), dtype=np.uint8)

# Bitwise OR untuk gabungkan karakter dan background
bitwise_or = cv2.bitwise_or(canvas, background)
cv2.imwrite("output/bitwise.png", bitwise_or)

# Aritmatika add
added = cv2.add(canvas, background)
cv2.imwrite("output/final.png", added)

# Tampilkan hasil (opsional)
# Tekan tombol apa saja untuk menutup jendela
cv2.imshow("Karakter", canvas)
cv2.imshow("Translate", translated)
cv2.imshow("Rotate", rotated)
cv2.imshow("Resize", resized)
cv2.imshow("Crop", cropped)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Final Add", added)
cv2.waitKey(0)
cv2.destroyAllWindows()