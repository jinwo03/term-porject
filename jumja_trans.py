import pytesseract
import cv2 
import matplotlib.pyplot as plt
from jamo import h2j, j2hcj
import hbcvt

img_path = "gall2.png"
image = cv2.imread(img_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(rgb_image, lang='kor+eng')

jamo_str = j2hcj(h2j(text))

zum = [[0 for col in range(len(jamo_str))] for row in range(len(jamo_str))]
count = 0
h = hbcvt.h2b.text(text)

for x in h:
    y = x[1]
    for z in y:
        w = z[1]
        q = w[0]
        zum[count] = q
        count = count+1


lx = [0 for i in range(len(zum)*6)]
ly = [0 for i in range(len(zum)*6)]
first_x = 0
first_y = 30
y = 300
count=0
for x in zum:
    if first_x == 300:
        first_x=0
        y= y -40
    first_x = first_x + 10
    first_y = y
    for z in range(0, 6):
        if z ==3:
            first_x = first_x + 10
            first_y = y
        if x[z]==1:
            lx[count] = first_x
            ly[count] = first_y
            first_y = first_y - 10
            count = count+1
        else:
            first_y = first_y - 10
cv2.imshow("image", image)
plt.scatter(lx, ly, marker='o', s=30, c='black', edgecolors='black')

plt.title('Braille')
plt.axis('off')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
