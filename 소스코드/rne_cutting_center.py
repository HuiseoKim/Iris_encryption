from PIL import Image
r=300
a=496
b=320
img = Image.open("croped/iris1.bmp")
area = (a-r,b-r,a+r,b+r)
cropped_img = img.crop(area)
cropped_img.save('croped/Centered_image.png')
