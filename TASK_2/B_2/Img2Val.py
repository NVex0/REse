from PIL import Image
img = Image.open("D:\Downloads\dn.png")
pixel = img.load()

with open ("rgbaval.txt", "w") as f:
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b, a = pixel[x, y]
            f.write("(" + str(r) + "," + str(g) + "," + str(b) + ") ")
        f.write("\n")
