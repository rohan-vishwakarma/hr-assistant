from data.employees import employees

def employee_list(employee_id: str = None) -> dict:
    """
    Return employee data as well as based on employee Id. 
    """
    return employees.get(employee_id, {"error": "Employee Not Found"})
