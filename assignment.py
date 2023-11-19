
def add_employee():
    """
    Function to add a new employee to the database.
    """

    employee_number = int(input("Enter employee number: "))

    """
    Prompt for employee ID, first name, last name, date of birth, sex,
    year of recruitment, and salary.
    """
    employee_id = input(f"Enter Employee ID for employee {employee_number}: ")
    first_name = input(f"Enter First Name for employee {employee_number}: ")
    last_name = input(f"Enter Last Name for employee {employee_number}: ")
    date_of_birth = input(f"Enter Date of Birth (YYYY-MM-DD) for employee {employee_number}: ")
    sex = input(f"Enter Sex (M/F) for employee {employee_number}: ")
    year_of_recruitment = int(input(f"Enter Year of Recruitment for employee {employee_number}: "))
    salary = float(input(f"Enter Salary for employee {employee_number}: "))

    """
    Create a dictionary containing the employee's information.
    """
    employee_dict = {
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "sex": sex,
        "year_of_recruitment": year_of_recruitment,
        "salary": salary
    }

    """
    Add the employee dictionary to the employees list.
    """
    employees.append(employee_dict)


def display_employees():
    """
    Function to display information for all employees.
    """
    for employee_number, employee in enumerate(employees, 1):
        """
        Enumerate through the employees list, assigning an employee number
        starting from 1.
        """
        print(f"Information of Employee {employee_number}:")

        """
        Print each employee's information.
        """
        print("Employee ID:", employee["employee_id"])
        print("First Name:", employee["first_name"])
        print("Last Name:", employee["last_name"])
        print("Date of Birth:", employee["date_of_birth"])
        print("Sex:", employee["sex"])
        print("Year of Recruitment:", employee["year_of_recruitment"])
        print("Salary:", employee["salary"])
        print()

# Initialize the employee database
employees = []

# Get the number of employees to enter
num_employees = int(input("Enter the number of employees: "))

# Add each employee's information
for i in range(num_employees):
    add_employee()

# Display all employees
display_employees()
