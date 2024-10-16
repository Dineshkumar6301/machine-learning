import pandas as pd

# Sample order data
order_data = {
    'order_id': [1, 2, 3, 4],
    'pickup_location': ['Location A', 'Location B', 'Location A', 'Location C'],
    'delivery_location': ['Location B', 'Location C', 'Location D', 'Location A'],
    'order_time': ['12:30', '12:35', '12:40', '12:50'],
    'delivery_deadline': ['13:15', '13:20', '13:30', '13:35'],
    'status': ['pending', 'pending', 'pending', 'pending']
}

# Sample rider data
rider_data = {
    'rider_id': [101, 102, 103, 104],
    'current_location': ['Location A', 'Location B', 'Location C', 'Location D'],
    'capacity': [2, 1, 3, 2],
    'availability': ['free', 'free', 'free', 'free'],
    'status': ['idle', 'idle', 'idle', 'idle']
}

# Convert to DataFrame
orders_df = pd.DataFrame(order_data)
riders_df = pd.DataFrame(rider_data)

# Save DataFrame to CSV files
orders_df.to_csv('orders.csv', index=False)
riders_df.to_csv('riders.csv', index=False)

print("CSV files have been created successfully.")
