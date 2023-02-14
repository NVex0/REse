from PIL import Image
img = Image.open("D:\Downloads\ys.png")
pix = img.load()
cipimg = Image.new(img.mode, img.size)
cippix = cipimg.load()

def lenbuf(val):
    while len(val) < 8:
        val = '0' + val
    return val

name = "Tran_Manh_Hung"
cipherb = ""
for i in name:
    cipherb += lenbuf(bin(ord(i))[2:])
index = 0

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b, a = pix[x, y]
        if index < len(cipherb):
            nr = lenbuf(bin(r)[2:])
            nr = int(nr[:6] + cipherb[index] + nr[-1:], 2)
            index += 1
        else:
            nr = r
        if index < len(cipherb): 
            ng = lenbuf(bin(g)[2:])
            ng = int(ng[:7] + cipherb[index], 2)
            index += 1
        else:
            ng = g
        if index < len(cipherb):
            nb = lenbuf(bin(b)[2:])
            nb = int(nb[:5] + cipherb[index] + nb[-2:], 2)
            index += 1
        else:
            nb = b
        cippix[x, y] = nr, ng, nb

cipimg.save("D:\Downloads\ys2nd.png")