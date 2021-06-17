import sys
import matplotlib.pyplot as plt
import pandas as pd

fn = sys.argv[1]

df = pd.read_csv(fn)

diffs = df['trial.started'].diff()
diffs = diffs[diffs != diffs.max()]
plt.hist(diffs)
plt.show()
