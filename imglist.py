import os

def Test(rootdir, file):
  list_dirs = os.walk(rootdir)
  for root, dirs, files in list_dirs:
    for f in files:
      path = os.path.join(root, f)
      label = os.path.relpath(root, rootdir)
      if f.endswith(".png"):
        file.write(path +"\t" + label +"\n")

      
  """
  for lists in os.listdir(rootdir):
    path = os.path.join(rootdir, lists)
    if lists.endswith(".png"):
      file.write(path + "\n")
      print os.path.relpath(root, directory)
    if os.path.isdir(path):
      Test(path,file)
  """
  
if __name__ == '__main__':
  """
  ftrain = open("train.txt", "w")
  Test("./mnist_png/training",ftrain)
  ftrain.close()
  ftest = open("test.txt", "w")
  Test("./mnist_png/testing",ftest)
  ftrain.close()
  """
  path = []
  with open("test.txt","r") as f:
    lines = f.readlines()
    for line in lines:
      item = line.split("\t")
      print item[0]
