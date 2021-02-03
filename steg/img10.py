from PIL import Image

img_in = Image.open("outputImage1.png")
img_out = Image.open("inputImage.png")

pixels_in = img_in.load()
pixels_out = img_out.load()

combined = Image.new(img_in.mode, img_in.size, color = 'black')
pixels_combined = combined.load()

w, h = img_in.size

for x in range(w):
    for y in range(h):
        p_in = pixels_in[x, y]
        p_out = pixels_out[x, y]

        # if p_out[0] == 255:
        print(p_out[0] == 255)
        print(p_in)
            # break

        # print(p_in)
        # print(p_out)
        # print()


        # r = p_a[0] + p_b[0]
        # g = p_a[1] + p_b[1]
        # b = p_a[2] + p_b[2]
        # pixels_combined[x, y] = (r, g, b, 255)
        if y == 210:
            break    # break
    break


# combined.save("testout.png")
