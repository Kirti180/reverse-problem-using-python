employee = [
    {"name": "kirti", "salary": 10000, "designation": "employee"},
    {"name": "abc", "salary": 1000, "designation": "employee"},
]

def high_employee(employees):
    if not employees:
        return None
    high = float('-inf')
    high_employee = None
    for emp in employees:
        if 'salary' in emp:
            salary = emp['salary']
            if salary > high:
                high = salary
                high_employee = emp
    return high_employee

details = high_employee(employee)
print(details)
