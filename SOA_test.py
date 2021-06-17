import sys
import matplotlib.pyplot as plt
import pandas as pd

fn = sys.argv[1]

df = pd.read_csv(fn)

diffs = df['trial.started'].diff()
diffs = diffs[diffs != diffs.max()]
plt.hist(diffs)
plt.ticklabel_format(style='plain', useOffset=False)
plt.show()
plt.plot(diffs)
plt.ticklabel_format(style='plain', useOffset=False)
plt.show()
