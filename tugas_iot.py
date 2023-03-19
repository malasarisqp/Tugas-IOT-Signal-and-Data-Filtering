import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('datafix.xlsx')
data = pd.DataFrame(data)
data

"""# LPF"""

cut = 20
freq = 85
lpf = pd.DataFrame()
df = pd.read_excel('datafix.xlsx', header = None)
for i in range(0, len(df), freq) :
  lpf = pd.concat([lpf, df[i:i+cut]])
fig, frq = plt.subplots(figsize=(10,10))
frq.plot(df[1], label = 'mentah')
frq.plot(lpf[1], label = 'hasil filter', color = 'red')
plt.legend()
plt.show()

"""# MVA"""

mva = pd.DataFrame()
df = pd.read_excel('datafix.xlsx', header = None)
tmp = df.iloc[:,2].rolling(window=2).mean()
plt.figure(figsize=(10,10))
plt.plot(tmp)
plt.legend()
plt.show()