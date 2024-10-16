import pandas as pd
import streamlit as st

# Sample function to assign riders to orders
def assign_riders(orders, riders):
    assignments = []
    for index, order in orders.iterrows():
        if len(riders) > 0:
            # Get the first available rider
            rider = riders.iloc[0]
            
            # Append the order_id and rider_id assignment
            assignments.append((order['order_id'], rider['rider_id']))
            
            # Remove the assigned rider from the riders DataFrame
            riders = riders.iloc[1:].reset_index(drop=True)  # Remove the first row (rider)
        else:
            st.warning("Not enough riders to assign to all orders!")
            break
    
    return assignments, orders, riders

# Example data (replace with your CSV loading logic)
orders_data = {'order_id': [1, 2, 3], 'order_time': ['10:00', '10:05', '10:10']}
riders_data = {'rider_id': [101, 102, 103], 'available': [True, True, True]}

orders = pd.DataFrame(orders_data)
riders = pd.DataFrame(riders_data)

# Call the function
assignments, updated_orders, updated_riders = assign_riders(orders, riders)

# Show the result in Streamlit
st.write("Assignments:")
st.write(assignments)
