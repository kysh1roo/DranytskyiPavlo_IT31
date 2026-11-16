from pathlib import Path
import lab_work_1 as files


directory = Path.home() / "Desktop"


print("Список файлів на робочому столі:")
print(files.list_files(directory))


print("\nПошук файлів, у назві яких є 'py':")
print(files.find_files(directory, "py"))


file_path = Path(__file__).parent / "pavlo_dranytskyi.txt"

files.create_file(
    file_path,
    "Ім'я: Павло\n"
    "Прізвище: Драницький\n"
    "Група: ІТ-31"
)

print("\nСтворено файл:", file_path.name)