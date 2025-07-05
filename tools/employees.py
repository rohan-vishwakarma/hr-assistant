from data.employees import employees

def employee_list(employee_id: str = None) -> dict:
    """
    Return employee data as well as based on employee id.
    """
    if not employee_id:
        return employees
    
    if not isinstance(employees, dict):
        return {"error": "Internal data error"}

    return employees.get(employee_id, {"error": "Employee not found"})
