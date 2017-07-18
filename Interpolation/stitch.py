from PIL import Image as im

def stitcher(im1, im2, file_name="derivation", padding = 10):
    im1, im2 = im.open(str(im1)), im.open(str(im2))
    size1, size2 = im1.size, im2.size
    size = [max(size1[i], size2[i]) for i in range(2)]
    size[1] = size1[1] + size2[1]
    new_img = im.new("RGBA", (size[0]+padding, size[1]+ padding), "white")
    new_img.paste(im1, (0+int(padding/2), 0+int(padding/2), size1[0]+int(padding/2), size1[1]+int(padding/2)))
    # print((0, 0) + size1)
    # print((0, size1[1], size2[0], size1[1]+size2[1]))
    new_img.paste(im2, (0+int(padding/2), size1[1]+int(padding/2), size2[0]+int(padding/2), size1[1]+size2[1]+int(padding/2)))
    new_img.save(file_name + ".png", "png")
