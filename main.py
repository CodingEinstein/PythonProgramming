from PIL import Image
import random
import image_class as IMAGE


img = Image.open("DICE_EMPTY.jpg")
img.load()
img2 = Image.open("DICE_EMPTY.jpg")
img2.load()
point = Image.open("DICE_POINT_edited.png")
point.load()


def gen_dice(num, count):
    if count == 1:
        if num == 1:
            img.paste(point, (500, 1000), mask=point)
            IMAGE.dice1 = img
            IMAGE.dice1.save("dice1.jpg")
        if num == 2:
            img.paste(point, (650, 1150), mask=point)
            img.paste(point, (350, 850), mask=point)
            IMAGE.dice1 = img
            IMAGE.dice1.save("dice1.jpg")
        if num == 3:
            img.paste(point, (650, 1150), mask=point)
            img.paste(point, (350, 850), mask=point)
            img.paste(point, (500, 1000), mask=point)
            IMAGE.dice1 = img
            IMAGE.dice1.save("dice1.jpg")
        if num == 4:
            img.paste(point, (650, 1150), mask=point)
            img.paste(point, (350, 850), mask=point)
            img.paste(point, (350, 1149), mask=point)
            img.paste(point, (650, 850), mask=point)
            IMAGE.dice1 = img
            IMAGE.dice1.save("dice1.jpg")
        if num == 5:
            img.paste(point, (650, 1150), mask=point)
            img.paste(point, (350, 850), mask=point)
            img.paste(point, (350, 1149), mask=point)
            img.paste(point, (500, 1000), mask=point)
            img.paste(point, (650, 850), mask=point)
            IMAGE.dice1 = img
            IMAGE.dice1.save("dice1.jpg")
        if num == 6:
            img.paste(point, (650, 1150), mask=point)
            img.paste(point, (350, 850), mask=point)
            img.paste(point, (350, 1000), mask=point)
            img.paste(point, (650, 1000), mask=point)
            img.paste(point, (350, 1149), mask=point)
            img.paste(point, (650, 850), mask=point)
            IMAGE.dice1 = img
            IMAGE.dice1.save("dice1.jpg")
    else:
        if num == 1:
            img2.paste(point, (500, 1000), mask=point)
            IMAGE.dice2 = img2
            IMAGE.dice2.save("dice2.jpg")
        if num == 2:
            img2.paste(point, (650, 1150), mask=point)
            img2.paste(point, (350, 850), mask=point)
            IMAGE.dice2 = img2
            IMAGE.dice2.save("dice2.jpg")
        if num == 3:
            img2.paste(point, (650, 1150), mask=point)
            img2.paste(point, (350, 850), mask=point)
            img2.paste(point, (500, 1000), mask=point)
            IMAGE.dice2 = img2
            IMAGE.dice2.save("dice2.jpg")
        if num == 4:
            img2.paste(point, (650, 1150), mask=point)
            img2.paste(point, (350, 850), mask=point)
            img2.paste(point, (350, 1149), mask=point)
            img2.paste(point, (650, 850), mask=point)
            IMAGE.dice2 = img2
            IMAGE.dice2.save("dice2.jpg")
        if num == 5:
            img2.paste(point, (650, 1150), mask=point)
            img2.paste(point, (350, 850), mask=point)
            img2.paste(point, (350, 1149), mask=point)
            img2.paste(point, (500, 1000), mask=point)
            img2.paste(point, (650, 850), mask=point)
            IMAGE.dice2 = img2
            IMAGE.dice2.save("dice2.jpg")
        if num == 6:
            img2.paste(point, (650, 1150), mask=point)
            img2.paste(point, (350, 850), mask=point)
            img2.paste(point, (350, 1000), mask=point)
            img2.paste(point, (650, 1000), mask=point)
            img2.paste(point, (350, 1149), mask=point)
            img2.paste(point, (650, 850), mask=point)
            IMAGE.dice2 = img2
            IMAGE.dice2.save("dice2.jpg")


n1 = int(random.uniform(1, 7))
n2 = int(random.uniform(1, 7))
gen_dice(n1, 1)
gen_dice(n2, 2)
print(n1, n2)
result = Image.new('RGB', (2160, 1440))
result.load()
IMAGE.dice1.load()
IMAGE.dice2.load()
result.paste(IMAGE.dice1, (0, 0))
result.paste(IMAGE.dice2, (1080, 0))
result.save("dice_result.jpg")
result.show()
move_points = n1 + n2
print("You got", move_points, "points!")
