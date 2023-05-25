import numpy as np
from PIL import Image, ImageDraw
import cv2

img10=Image.open("croped/Croped_radius_7.png")
img20=Image.open("croped/Croped_radius_45.png")
img30=Image.open("croped/Croped_radius_35.png")
img40=Image.open("croped/Croped_radius_14.png")
img50=Image.open("croped/Croped_radius_43.png")
img60=Image.open("croped/Croped_radius_76.png")
img70=Image.open("croped/Croped_radius_73.png")
img80=Image.open("croped/Croped_radius_0.png")
Image.alpha_composite(img20,img10).save("croped/total.png")
total=Image.open("croped/total.png")
Image.alpha_composite(img30,total).save("croped/total.png")
total=Image.open("croped/total.png")
Image.alpha_composite(img40,total).save("croped/total.png")
total=Image.open("croped/total.png")
Image.alpha_composite(img50,total).save("croped/total.png")
total=Image.open("croped/total.png")
Image.alpha_composite(img60,total).save("croped/total.png")
total=Image.open("croped/total.png")
Image.alpha_composite(img70,total).save("croped/total.png")
total=Image.open("croped/total.png")
Image.alpha_composite(img80,total).save("croped/total.png")

