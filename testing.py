import os

path1 = "C:\\Users\\alexr\\PycharmProjects\\bot1\\img_training\\"

i = 1
for filename in os.listdir(path=path1):
    src = path1 + filename
    dst = path1 + "menhera" + str(i) + ".png"
    os.rename(src, dst)
    i += 1
