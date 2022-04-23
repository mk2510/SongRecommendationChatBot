import numpy as np
import matplotlib.pyplot as plt

data  = [0.37211666850418007, 0.4937262279795504, 0.5456832346447217, 0.31220945733240824, 0.8266875235549795, 0.505935286273305]
labels = ['','Doc2Vec', 'USE', 'BERT', 'TFIDF', 'GloVE', 'FastText']

ax1 = plt.subplot()
ax1.set_ylabel('cosine similariy')
ax1.set_xlabel('Methods')
plt.bar(range(len(data)), data)
ax1.set_xticklabels(labels) 
plt.savefig('uncleanded.pdf')
plt.show()