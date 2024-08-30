from zipfile import *

f = ZipFile("images.zip", "w", ZIP_DEFLATED)

f.write("c#.png")
f.write("js.png")
f.write("python.jpg")

f.close()