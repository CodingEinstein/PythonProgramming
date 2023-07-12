from PIL import Image
import random

n1 = int(random.uniform(1, 6))

n2 = int(random.uniform(1, 6))
while n1 > n2:
    n1 = int(random.uniform(1, 6))
    n2 = int(random.uniform(1, 6))
    if n1 > n2:
        n1 = int(random.uniform(1, 6))
        n2 = int(random.uniform(1, 6))
    else:
        break
while n1 == 1 or n2 == 1:
    n1 = int(random.uniform(1, 6))
    n2 = int(random.uniform(1, 6))
    if n1 == 1 or n2 == 1:
        n1 = int(random.uniform(1, 6))
        n2 = int(random.uniform(1, 6))
    else:
        break
while n1 + n2 == 5:
    n1 = int(random.uniform(1, 6))
    n2 = int(random.uniform(1, 6))
    if n1 + n2 == 5:
        n1 = int(random.uniform(1, 6))
        n2 = int(random.uniform(1, 6))
    else:
        break
img = Image.open("DICE_EMPTY.jpg")
img.load()
point = Image.open("DICE_POINT_edited.png")
point.load()
if n1 == 1:
    img.paste(point, (500, 1000), mask=point)
if n1 == 2:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
if n1 == 3:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (500, 1000), mask=point)
if n1 == 4:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (350, 1149), mask=point)
    img.paste(point, (650, 850), mask=point)
if n1 == 5:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (350, 1149), mask=point)
    img.paste(point, (500, 1000), mask=point)
    img.paste(point, (650, 850), mask=point)
if n1 == 6:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (350, 1000), mask=point)
    img.paste(point, (650, 1000), mask=point)
    img.paste(point, (350, 1149), mask=point)
    img.paste(point, (650, 850), mask=point)
dice1 = img
dice1.save("dice1.jpg")
if n2 == 1:
    img.paste(point, (500, 1000), mask=point)
if n2 == 2:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
if n2 == 3:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (500, 1000), mask=point)
if n2 == 4:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (350, 1149), mask=point)
    img.paste(point, (650, 850), mask=point)
if n2 == 5:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (350, 1149), mask=point)
    img.paste(point, (500, 1000), mask=point)
    img.paste(point, (650, 850), mask=point)
if n2 == 6:
    img.paste(point, (650, 1150), mask=point)
    img.paste(point, (350, 850), mask=point)
    img.paste(point, (350, 1000), mask=point)
    img.paste(point, (650, 1000), mask=point)
    img.paste(point, (350, 1149), mask=point)
    img.paste(point, (650, 850), mask=point)
dice2 = img
dice2.save("dice2.jpg")
print(n1, n2)
result = Image.new('RGB', (2160, 1440))
result.load()
dice1.load()
dice2.load()
result.paste(dice1, (0, 0))
result.paste(dice2, (1080, 0))
result.save("dice_result.jpg")
