 import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Find days where temperature exceeded 35°C (hot days)
hot_days = temperatures > 35.0

# Find days where temperature dropped below 5°C (cold days)
cold_days = temperatures < 5.0

# Combine the conditions to find extreme temperature days
extreme_temperature_days = np.logical_or(hot_days, cold_days)

# Print the indices of the extreme temperature days
print("Indices of extreme temperature days:", np.where(extreme_temperature_days)[0])

# Print the temperatures on extreme temperature days
print("Temperatures on extreme temperature days:", temperatures[extreme_temperature_days])
 Indices of extreme temperature days: [2 5 6 7]cold days
Temperatures on extreme temperature days: [36.8 38.7 23.1 18.5]hot days
