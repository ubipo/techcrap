from PIL import Image

img_a = Image.open("testouta.png")
img_b = Image.open("testoutb.png")

pixels_a = img_a.load()
pixels_b = img_b.load()

combined = Image.new(img_a.mode, img_a.size, color = 'black')
pixels_combined = combined.load()

w, h = img_a.size

for x in range(w):
    for y in range(h):
        p_a = pixels_a[x, y]
        p_b = pixels_b[x, y]
        r = p_a[0] + p_b[0]
        g = p_a[1] + p_b[1]
        b = p_a[2] + p_b[2]
        pixels_combined[x, y] = (r, g, b, 255)

combined.save("testout.png")
