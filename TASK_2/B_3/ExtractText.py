from PIL import Image
#Extract Text.
img = Image.open("D:\Downloads\ys2nd.png")
cippix = img.load()
def supportf(out, bina):
    if len(out) < 8:
        out += bina
    else:
        print(chr(int(out, 2)), end = "")
        out = bina
    return out
    
def lenbuf(val):
    while len(val) < 8:
        val = '0' + val
    return val
    
out = ""
loop = 0
for x in range(img.size[0]):
    for y in range(img.size[1]):
        vr, vg, vb, a = cippix[x, y]
        br = lenbuf(bin(vr)[2:])[6]
        bg = lenbuf(bin(vg)[2:])[7]
        bb = lenbuf(bin(vb)[2:])[5]
        out = supportf(out, br)
        out = supportf(out, bg)
        out = supportf(out, bb)
        loop += 1
        if loop == 40:
            exit()