class Student:
    college = "FKTBP VNU"   # атрибут класу (спільний для всіх)
    count = 0               # лічильник створених об'єктів

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self):
        return f"{self.name} {self.surname}"

    def age(self, year):
        return year - self.birth_year

    def card(self, year=2026):
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in {year}: {self.age(year)}",
        ]
        width = max(len(line) for line in lines)
        border = "+" + "-" * (width + 2) + "+"
        body = [f"| {line.ljust(width)} |" for line in lines]
        return "\n".join([border, *body, border])


if __name__ == "__main__":
    me = Student("Pavlo", "Dranytskyi", "IT-31", 2009)
    friend = Student("Vlad", "Panasiuk", "IT-31", 2009)
    print(me.card())
    print(friend.card())
