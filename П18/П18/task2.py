from task1 import Student

me = Student("Pavlo", "Dranytskyi", "IT-31", 2009)
friend = Student("Vlad", "Panasiuk", "IT-31", 2009)

print("college via class:   ", Student.college)
print("college via me:      ", me.college)
print("college via friend:  ", friend.college)

# Присвоєння через об'єкт створює НОВИЙ атрибут екземпляра,
# атрибут класу при цьому не змінюється.
me.college = "Another college"
print("\nafter me.college = 'Another college':")
print("me.college:          ", me.college)
print("friend.college:      ", friend.college)
print("Student.college:     ", Student.college)

print("\nme.__dict__:     ", me.__dict__)
print("friend.__dict__: ", friend.__dict__)
print("'college' in Student.__dict__:", "college" in Student.__dict__)
print("Student.__dict__['college']:  ", Student.__dict__["college"])

print("\nstudents created:", Student.count)
