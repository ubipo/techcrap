from PIL import Image
from collections import Counter

in_a = Image.open("riddle/riddleOutputImage3a.png")
in_b = Image.open("riddle/riddleOutputImage3b.png")

in_c = Image.open("riddle/riddleOutputImage3c.png")
in_d = Image.open("riddle/riddleOutputImage3d.png")

pixels_a = in_a.load()
pixels_b = in_b.load()
pixels_c = in_c.load()
pixels_d = in_d.load()

out_a = Image.new(in_a.mode, in_a.size, color = 'black')
out_b = Image.new(in_a.mode, in_a.size, color = 'black')

pixels_out_a = out_a.load()
pixels_out_b = out_b.load()

w, h = in_a.size

def inv_dict(dic):
    return {v: k for k, v in dic.items()}

for x in range(w):
    for y in range(h):
        p_a = pixels_a[x, y]
        p_b = pixels_b[x, y]
        p_c = pixels_c[x, y]
        p_d = pixels_d[x, y]

        counter_r_inv = inv_dict(Counter([p_a[0], p_b[0], p_c[0], p_d[0]]))
        counter_g_inv = inv_dict(Counter([p_a[1], p_b[1], p_c[1], p_d[1]]))
        counter_b_inv = inv_dict(Counter([p_a[2], p_b[2], p_c[2], p_d[2]]))

        r_a = sorted(counter_r_inv.items(), key=lambda v: v[0])[0][1]
        g_a = sorted(counter_g_inv.items(), key=lambda v: v[0])[0][1]
        b_a = sorted(counter_b_inv.items(), key=lambda v: v[0])[0][1]
        r_b = sorted(counter_r_inv.items(), key=lambda v: v[0])[-1][1]
        g_b = sorted(counter_g_inv.items(), key=lambda v: v[0])[-1][1]
        b_b = sorted(counter_b_inv.items(), key=lambda v: v[0])[-1][1]
        p_out_a = (r_a, g_a, b_a, 255)
        p_out_b = (r_b, g_b, b_b, 255)

        pixels_out_a[x, y] = p_out_a
        pixels_out_b[x, y] = p_out_b

out_a.save("testouta.png")
out_b.save("testoutb.png")
