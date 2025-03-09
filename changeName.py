import os

dir = "../10th"

files = os.listdir(dir)
index = 0
for file in files:
    filename = os.path.join(dir, file)

    f, e = os.path.splitext(filename)
    saveFileName = os.path.join(dir, str(index) + e)
    os.rename(filename, saveFileName)

    index += 1