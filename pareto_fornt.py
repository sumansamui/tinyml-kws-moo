import pandas as pd
import numpy as np

# Function to identify Pareto-optimal points
def is_pareto_efficient(costs):
    """
    Find the indices of Pareto-efficient points.
    Args:
        costs (np.ndarray): Array of costs where each row represents a point, and each column represents a criterion.
    Returns:
        np.ndarray: Indices of Pareto-efficient points.
    """
    is_efficient = np.ones(costs.shape[0], dtype=bool)  # Initially, assume all points are efficient
    for i, c in enumerate(costs):
        if is_efficient[i]:
            # Keep only points that are not strictly worse than the current point
            is_efficient[is_efficient] = (
                np.any(costs[is_efficient] < c, axis=1) | 
                np.all(costs[is_efficient] == c, axis=1)
            )
            is_efficient[i] = True  # Keep the current point
    return np.where(is_efficient)[0]

# Load the Excel file
file_path = 'D:\\SNgarai\\OneDrive\\SOUMEN\\New paper\\Multi_Objective\\result\\all_pareto.xlsx'  # Replace with your file path

# Save Pareto-optimal front to a new Excel file
output_file_path = 'D:\\SNgarai\\OneDrive\\SOUMEN\\New paper\\Multi_Objective\\result\\all__pareto_optimal_front.xlsx'  # Replace with desired output file name
df = pd.read_excel(file_path)

# Calculate costs based on accuracy and model size
costs = df[['accuracy', 'model_size']].copy()
costs['accuracy'] = 1 - costs['accuracy']  # Convert accuracy to cost
costs = costs.values

# Identify Pareto-optimal indices
pareto_indices = is_pareto_efficient(costs)

# Extract Pareto-optimal rows
pareto_front = df.iloc[pareto_indices]
pareto_front.to_excel(output_file_path, index=False)
print(f"Pareto-optimal front saved to {output_file_path}")