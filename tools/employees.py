from data.employees import employees

def employee_list(employee_id: str = None) -> dict:
    """
    Returns employee data by ID.
    """
    if not employee_id:
        return employees
    
    if not isinstance(employees, dict):
        return {"error": "Internal data error"}

    return employees.get(employee_id, {"error": "Employee not found"})
