 import numpy as np

# Employee data for full-time employees:
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees:
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine both arrays along the rows to create a comprehensive employee dataset
comprehensive_employee_data = np.concatenate((full_time_employees, part_time_employees), axis=0)

# Print the combined dataset
print("Comprehensive Employee Dataset:")
print(comprehensive_employee_data)
 Comprehensive Employee Dataset:
[[101 'John Doe' 'Full-Time' 55000]
 [102 'Jane Smith' 'Full-Time' 60000]
 [103 'Mike Johnson' 'Full-Time' 52000]
 [201 'Alice Brown' 'Part-Time' 25000]
 [202 'Bob Wilson' 'Part-Time' 28000]
 [203 'Emily Davis' 'Part-Time' 22000]]
