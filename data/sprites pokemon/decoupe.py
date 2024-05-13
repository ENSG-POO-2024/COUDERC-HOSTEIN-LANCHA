import cv2

img = cv2.imread("all_sprites.png")

x0 = 0
y0 = 0

for k in range(1, 153):
    i = (k - 1) // 26
    j = (k - 1) % 26
    x0 = 570 + i * 651
    y0 = 18 + j * 131
    x1 = x0 + 56
    y1 = y0 + 56
    if k < 124:
        roi = img[y0:y1, x0:x1]
        nom_fichier = f"{k}.jpg"
        cv2.imwrite(nom_fichier, roi)
    elif k > 124:
        roi = img[y0:y1, x0:x1]
        nom_fichier = f"{k-1}.jpg"
        cv2.imwrite(nom_fichier, roi)
