from PIL import Image
import random


img = Image.open("DICE_EMPTY.jpg")
img.load()
img2 = Image.open("DICE_EMPTY.jpg")
img2.load()
point = Image.open("DICE_POINT_edited.png")
point.load()


def gen_dice(num, image_obj, savename):
    if num == 1:
        image_obj.paste(point, (500, 1000), mask=point)
        image_obj.save(savename)
        return image_obj
    if num == 2:
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.save(savename)
        return image_obj
    if num == 3:
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (500, 1000), mask=point)
        image_obj.save(savename)
        return image_obj
    if num == 4:
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (350, 1149), mask=point)
        image_obj.paste(point, (650, 850), mask=point)
        image_obj.save(savename)
        return image_obj
    if num == 5:
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (350, 1149), mask=point)
        image_obj.paste(point, (500, 1000), mask=point)
        image_obj.paste(point, (650, 850), mask=point)
        image_obj.save(savename)
        return image_obj
    if num == 6:
        image_obj.paste(point, (650, 1150), mask=point)
        image_obj.paste(point, (350, 850), mask=point)
        image_obj.paste(point, (350, 1000), mask=point)
        image_obj.paste(point, (650, 1000), mask=point)
        image_obj.paste(point, (350, 1149), mask=point)
        image_obj.paste(point, (650, 850), mask=point)
        image_obj.save(savename)
        return image_obj


if __name__ == "__main__":
    n1 = int(random.uniform(1, 7))
    n2 = int(random.uniform(1, 7))
    dice1 = gen_dice(n1, img, "dice1.jpg")
    dice2 = gen_dice(n2, img2, "dice2.jpg")
    print(n1, n2)
    result = Image.new('RGB', (2160, 1440))
    result.load()
    dice1.load()
    dice2.load()
    result.paste(dice1, (0, 0))
    result.paste(dice2, (1080, 0))
    result.save("dice_result.jpg")
    result.show()
    move_points = n1 + n2
    print("You got", move_points, "points!")
