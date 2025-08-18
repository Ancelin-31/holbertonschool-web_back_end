export default function createEmployeesObject(departmentName, employees) {
    let department = [];
    for (const [idx, value] of employees.entries()) {
    department[idx] = value;
  }

  return `${departmentName}: [${department}]`;
}
