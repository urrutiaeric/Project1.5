import csv 

class Staff:
    def __init__(self, name, id_num, role, filename="staff.csv"):
        self.name = name
        self.id_num = id_num
        self.role = role
        self.filename = filename

    def add_to_csv(self):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Staff", self.name, self.id_num, self.role])

    def __str__(self):
        return f"Staff Name: {self.name}, ID: {self.id_num}, Role: {self.role}"

