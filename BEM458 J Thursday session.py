#######################################################################################################################################################
# 
# Name: SYED MOHAMMED ARSH
# SID:750003168
# Exam Date:27 MARCH 2025
# Module: BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-Arsh48484
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Initialize an empty list to store (start, end) positions
my_list = []

# Loop through each key-value pair in the dictionary
for key, comment in key_comments.items():
    # Find the start position of the word
    start_pos = customer_feedback.find(comment)
    
    # Calculate the end position (start position + length of the word)
    end_pos = start_pos + len(comment)
    
    # Append the tuple (start_pos, end_pos) to the list
    my_list.append((start_pos, end_pos))

# Print the list of start and end positions
print(my_list)
#EXETED OUTPUT
[(12, 23), (7, 12), (36, 41), (60, 65), (122, 130), (98, 108), (22, 32), (80, 87), (34, 41), (62, 67)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here
# Insert first two digits of ID number here:
first_two_digits = 12  # Example, replace with actual digits

# Insert last two digits of ID number here:
last_two_digits = 34  # Example, replace with actual digits

# Operating Profit Margin
def operating_profit_margin(operating_profit, revenue):
    return (operating_profit / revenue) * 100

# Revenue per Customer
def revenue_per_customer(revenue, number_of_customers):
    return revenue / number_of_customers

# Customer Churn Rate
def customer_churn_rate(customers_lost, customers_start_period):
    return (customers_lost / customers_start_period) * 100

# Average Order Value
def average_order_value(total_revenue, total_orders):
    return total_revenue / total_orders

# Example values for calculations (you can replace them with your actual numbers)
operating_profit = first_two_digits * 1000  
revenue = last_two_digits * 10000  
number_of_customers = first_two_digits * 50  
customers_lost = last_two_digits * 5 
customers_start_period = first_two_digits * 200  
total_revenue = revenue  
total_orders = last_two_digits * 10  

# Call the functions and print the results
print(f"Operating Profit Margin: {operating_profit_margin(operating_profit, revenue):.2f}%")
print(f"Revenue per Customer: {revenue_per_customer(revenue, number_of_customers):.2f}")
print(f"Customer Churn Rate: {customer_churn_rate(customers_lost, customers_start_period):.2f}%")
print(f"Average Order Value: {average_order_value(total_revenue, total_orders):.2f}")

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data for price and demand
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# 1. Perform linear regression
model = LinearRegression()
model.fit(prices, demand)

# Get the coefficients (intercept and slope)
intercept = model.intercept_
slope = model.coef_[0]

# The linear regression equation
print(f"Linear Regression Equation: Demand = {intercept:.2f} + {slope:.2f} * Price")

# 2. Find the price that maximizes revenue
# Revenue function: R(P) = P * (intercept + slope * P)
# Take the derivative of the revenue function with respect to P and set it to zero to find the maximum
# d(R(P))/dP = 0 => intercept + 2 * slope * P = 0 => P = -intercept / (2 * slope)

max_revenue_price = -intercept / (2 * slope)
print(f"Price that maximizes revenue: £{max_revenue_price:.2f}")

# 3. Find the demand when price is £52
price_52_demand = model.predict(np.array([[52]]))
print(f"Demand when price is £52: {price_52_demand[0]:.2f} units")

# Plot the data and the linear regression line
plt.scatter(prices, demand, color='blue', label='Data points')
plt.plot(prices, model.predict(prices), color='red', label='Regression line')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Price vs. Demand')
plt.legend()
plt.grid(True)
plt.show()

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))  
random_numbers = [random.randint(1, max_value) for i in range(0, 100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
plt.title('Line Chart of 100 Random Numbers')  
plt.xlabel('Index')  
plt.ylabel('Random Number')  
plt.legend()  
plt.grid(True)
plt.show()



