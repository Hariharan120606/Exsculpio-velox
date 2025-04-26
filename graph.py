import pandas as pd
import matplotlib.pyplot as plt

# Benchmark data: Number of threads vs. time taken (seconds)
data = {
    'Threads': [1, 5, 10, 25, 50, 100],
    'Serial': [34.57, 34.57, 34.57, 34.57, 34.57, 34.57],
    'Parallel': [6.00, 4.12, 4.12, 1.50, 0.72, 0.36]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the benchmark results table
print(df)

# Plot the performance comparison
plt.figure()
plt.plot(df['Threads'], df['Serial'], marker='o', label='Serial', color='blue')
plt.plot(df['Threads'], df['Parallel'], marker='o', label='Parallel', color='orange')
plt.xlabel('Number of Threads')
plt.ylabel('Time (s)')
plt.title('Serial vs Parallel Scraping Performance')
plt.legend()
plt.tight_layout()
plt.show()
