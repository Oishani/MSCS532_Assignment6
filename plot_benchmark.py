import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('benchmark_results.csv')

for name in df['algorithm'].unique():
    sub = df[df['algorithm']==name]
    for dist in df['distribution'].unique():
        part = sub[sub['distribution']==dist]
        plt.plot(part['size'], part['avg_time_s'], label=f"{name}-{dist}")

plt.xlabel("Input size (n)")
plt.ylabel("Average time (s)")
plt.legend()
plt.title("Selection Algorithm Performance")
plt.savefig("benchmark_plot.png")
plt.show()