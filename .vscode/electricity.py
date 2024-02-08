def electricity_bill(CUSTOMER_ID, CUSTOMER_NAME, units):
    # Determine the electricity charge based on the units consumed
    if units <= 199:
        charge = units * 1.2
    elif units >= 200 and units <= 400:
        charge = 1.5 * units
    elif units >= 400 and units <= 600:
        charge = 1.80 * units
    elif units >= 600:
        charge = 2 * units
    
    # Return the calculated charge
    return charge

# Get input from the user for customer ID, customer name, and units consumed
CUSTOMER_ID = int(input("Enter customer ID: "))
CUSTOMER_NAME = input("Enter customer name: ")
UNIT_CONSUMED = int(input("Enter units consumed: "))

# Print the calculated electricity bill
print("Electricity bill for customer", CUSTOMER_NAME, "with ID", CUSTOMER_ID, "is:", electricity_bill(CUSTOMER_ID, CUSTOMER_NAME, UNIT_CONSUMED))
