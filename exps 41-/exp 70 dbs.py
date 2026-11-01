data = [
    ("Ananya", "pizza", 120),
    ("Nivasa", "Burger", 80),
    ("Lakshmi", "Sandwich", 60)
]

question = input("enter your question: ")

# Initialize variables to avoid errors if neither condition matches
sql = ""
result = []

if "pizza" in question.lower():
    sql = "SELECT * FROM orders2 WHERE food='Pizza';"
    result = [row for row in data if row[1] == "pizza"]
    
elif "burger" in question.lower():
    sql = "SELECT * FROM orders2 WHERE food='Burger';"
    result = [row for row in data if row[1] == "Burger"]

# Displays the results in the IDLE window
print("\nGenerated SQL Query:", sql)
print("Filtered Data:", result)
