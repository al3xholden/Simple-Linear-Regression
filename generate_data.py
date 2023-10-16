import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(0)

# Generate 'x' and 'y' values
x = np.random.uniform(1, 100, 300)
y = np.random.uniform(1, 100, 300)

# Create a DataFrame from the data
df = pd.DataFrame({'x': x, 'y': y})

# Save the DataFrame to a CSV file
df.to_csv('random_xy_data.csv', index=False)
