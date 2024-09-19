# Dictionary defining employee IDs, their names, and salaries
employees = {
    601001: {"Cassandra": 60500},
    601002: {"Steffany ": 68000},
    601003: {"Tristan  ": 72800},
    601004: {"Ashley   ": 105000}
}

# Variable initalizing salary increase of 8% annually
salary_increase = 0.08

# Prints current employee information
print("EMPLOYEE INFORMATION\n")
print("ID\tName\t   Salary")

# Nested for loop iterates through nested dictionary. Prints current salaries
# and employee information
for i, j in employees.items():
  for k,l in j.items():
    print(f"{i}\t{k}  ${l}")

# Prints updated employee information
print("\nUPDATED EMPLOYEE INFORMATION\n*Salary Increase of 8% Has Been Applied*\n")
print("ID\tName\t   Salary")

# Nested for loop iterates through nested dictionary, updating salaries with
# increases and prints them to the consoles.
for i, j in employees.items():
  for k,l in j.items():
    l *= (1 + salary_increase)
    print(f"{i}\t{k}  ${int(l)}")
