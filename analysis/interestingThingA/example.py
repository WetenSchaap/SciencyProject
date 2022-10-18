import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"/path/to/raw/data,csv")
df.dosomething()


fig,ax = plt.subplots(1,1)
ax.plot(df["x"],df["y"])
fig.savefig("tada.svg")
