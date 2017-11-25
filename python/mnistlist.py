import os
id_count = 1

def trace(rootdir, file, cls):
    """docstring for fname"""
    global id_count
    list_dirs = os.walk(rootdir)
    for root, dirs, files in list_dirs:
        for f in files:
            path = os.path.join(root, f)
            label = os.path.relpath(root, rootdir)
            if f.endswith(".png"):
                file.write(str(id_count) +","+str(f) +","+ str(cls) + "," + str(label) + "," + str(path) + "\n")
                id_count = id_count + 1
if __name__ == '__main__':
    file = open("mnistdata.txt","w")
    trace("./mnist_png/training", file, "train")
    trace("./mnist_png/testing", file, "test")
    file.close()
