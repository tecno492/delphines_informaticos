import stepic
from PIL import Image

file = "reto2_fondo.png"

img = Image.open(file)
deco = stepic.decode(img)

print("Data : " + deco)