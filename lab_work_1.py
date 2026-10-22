from pathlib import Path


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Параметри:
        directory (str): шлях до директорії.

    Результат:
        list: список назв файлів.
    """
    path = Path(directory)

    return sorted(
        file.name for file in path.iterdir()
        if file.is_file()
    )


def find_files(directory, substring):
    """
    Шукає файли, у назвах яких є вказаний підрядок.

    Параметри:
        directory (str): шлях до директорії.
        substring (str): підрядок для пошуку.

    Результат:
        list: список знайдених файлів.
    """
    files = list_files(directory)

    return [
        file for file in files
        if substring in file
    ]


def create_file(path, text):
    """
    Створює файл і записує в нього переданий текст.

    Параметри:
        path (str): шлях до нового файлу.
        text (str): текст для запису.

    Результат:
        str: шлях до створеного файлу.
    """
    file_path = Path(path)
    file_path.write_text(text, encoding="utf-8")

    return str(file_path)


if __name__ == "__main__":
    import tempfile

    print("Самоперевірка модуля")

    with tempfile.TemporaryDirectory() as directory:
        create_file(Path(directory) / "test.txt", "Тестовий файл")
        create_file(Path(directory) / "python.txt", "Python")

        print("Список файлів:", list_files(directory))
        print("Пошук файлів:", find_files(directory, "python"))

        created = create_file(
            Path(directory) / "result.txt",
            "Модуль працює правильно!"
        )

        print("Створено файл:", Path(created).name)