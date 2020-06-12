import pandas as pd
import glob
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Plots for all tech keywords
path = r'TechCSVs'
all_files = glob.glob(path + "/*.csv")
li = [pd.read_csv(filename, index_col='Day') for filename in all_files]
frame = pd.concat(li, axis=1, ignore_index=False)
frame.rename(columns=lambda x: x.rstrip('(United Kingdom)')[:-1], inplace=True)

frame.plot(subplots=True, layout=(4,4), figsize=(15,10))
plt.show()


# plt.plot(figsize=(150,50), kind='line')
# for col in frame.columns:
# 	plt.plot(frame[col], label = col)
# plt.title("Trends Over Time")
# plt.legend(loc="best", fontsize=8)
# plt.show()
