from PIL import Image

with open("rgbaval.txt", "r") as f:
    data = f.readlines()
    x = len(data)
    tmp = data[1].split(" ")
    y = len(tmp) - 1
        
imgsize = (x, y)
img = Image.new("RGB", imgsize)
pix = img.load()
for i in range (len(data)):
    temp = data[i].split(" ")
    for j in range (len(temp) - 1):
        t = temp[j][1:-1].split(",")
        t2 = (int(t[0]), int(t[1]), int(t[2]))
        pix[i, j] = t2
img.show()
    
