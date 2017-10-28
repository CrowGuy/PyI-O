import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
  x = []
  y = []
  data = []
  with open("data_example.txt") as file:
    data = file.read().split("\n")
    data.remove('')
    print data
    for row in data:
      tmp = row.split(",")
      print tmp
      x.append(int(tmp[0]))
      y.append(float(tmp[1])) 

    
  # Line plot
  plt.plot(x, y, color='red', linewidth=2.5, label="ORTC", marker='o')
  plt.xlabel('# of rules')
  plt.ylabel('Computation time (seconds)')
  plt.title('Computation time vs. # of rules')
  plt.legend(borderaxespad=0, bbox_to_anchor=(1.04,1))
  plt.subplots_adjust(right=0.8)
  plt.show()

  # Histogram plot 
  normal_samples = np.random.normal(size = 100000)
  plt.hist(normal_samples)
  plt.xlabel('')
  plt.ylabel('#')
  plt.title('Normal distribution')
  plt.show()
  
  # Scatter plot
  plt.scatter(x, y)
  plt.xlabel('# of rules')
  plt.ylabel('Computation time (seconds)')
  plt.title('Computation time vs. # of rules')
  plt.show()

  # Bar plot
  plt.xlabel('# of rules')
  plt.ylabel('Computation time (seconds)')
  plt.title('Computation time vs. # of rules')
  ind = np.arange(len(data))
  plt.xticks(ind,x)
  plt.bar(ind,y)
  plt.show()

  # Box plot
  plt.boxplot(y)
  plt.xlabel('Compression approach')
  plt.ylabel('Computation time (seconds)')
  plt.title('Computation time vs. # of rules')
  plt.show()
