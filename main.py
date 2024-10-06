def create_question_file():
    # Спробуємо виконати блок коду, що записує дані у файл
    try:
        # Створюємо (або відкриваємо) текстовий файл "student_question.txt" у режимі запису (w).
        # Використовуємо кодування UTF-8 для коректної обробки символів.
        with open("student_question.txt", "w", encoding="utf-8") as f:
            # Записуємо прізвище першого студента в файл
            f.write("Прізвище: Тихонов\n")
            # Записуємо питання, яке перший студент задає другому
            f.write("Питання: Як обробляти виключення в Python?\n")

        # Якщо операція пройшла успішно, виводимо повідомлення
        print("Файл із питанням успішно створено/редаговано.")

    # У разі виникнення помилки введення/виведення виконується цей блок
    except IOError:
        # Виводимо повідомлення про помилку, якщо файл не вдалося створити або записати
        print("Виникла помилка під час створення файлу.")

def read_and_print_file():
    # Спробуємо прочитати файл і вивести його вміст
    try:
        # Відкриваємо файл для читання
        with open("student_question.txt", "r", encoding="utf-8") as f:
            # Читаємо вміст файлу
            content = f.read()
            # Виводимо вміст на екран
            print("Вміст файлу:\n-------------")
            print(content)

    # У разі виникнення помилки читання виконується цей блок
    except IOError:
        print("Виникла помилка під час читання файлу.")

# Викликаємо створені функції
create_question_file()
read_and_print_file()