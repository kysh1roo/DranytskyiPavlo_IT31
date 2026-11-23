from task1 import GroupLeader, Person, Student

me = Student("Pavlo", "Dranytskyi", "IT-31")
leader = GroupLeader("Andrii", "Hordii", "IT-31", "+380 95 432 12 56")
classes = (Person, Student, GroupLeader)


def table(title, rows, row_label, check):
    print(title)
    header = f"{row_label:<14}" + "".join(f"{c.__name__:<14}" for c in classes)
    print(header)
    print("-" * len(header))
    for label, row in rows:
        print(f"{label:<14}" + "".join(f"{str(check(row, c)):<14}" for c in classes))
    print()


objects = (
    ("person", Person("Test", "Person")),
    ("me (Student)", me),
    ("leader", leader),
)
table("isinstance(object, Class):", objects, "object", isinstance)
table("issubclass(Class, Class):", [(c.__name__, c) for c in classes],
      "class", issubclass)

print("GroupLeader.__mro__:")
for cls in GroupLeader.__mro__:
    print(" ", cls.__name__)
print("\nisinstance(leader, Person):", isinstance(leader, Person))
