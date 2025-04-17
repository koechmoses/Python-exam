def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15):
    """
    Calculates the net salary of an employee.
    
    Parameters:
    hourly_rate (float): The amount paid per hour.
    hours_worked (float): The number of hours worked.
    tax_rate (float): The percentage of tax to deduct from gross salary (default is 15%).

    Returns:
    float: Net salary after tax deduction.
    """
    gross_salary = hourly_rate * hours_worked             # Step i: Calculate gross salary
    tax_deduction = gross_salary * tax_rate               # Step ii: Calculate tax
    net_salary = gross_salary - tax_deduction             # Step iii: Net salary after tax
    return net_salary

# Main program starts here
def main():
    try:
        # Step i: Prompt the user for input
        hourly_rate = float(input("Enter hourly rate: "))
        hours_worked = float(input("Enter hours worked: "))

        # Step iii: Validate input
        if hourly_rate < 0 or hours_worked < 0:
            print("Error: Hourly rate and hours worked must be non-negative numbers.")
            return

        # Step ii: Call function and print result
        net_salary = calculate_salary(hourly_rate, hours_worked)
        print(f"Net Salary: {net_salary:,.0f}")  # formatted with comma and no decimal places

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Call the main function to execute the program
main()






    










































