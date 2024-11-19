# Задание 1
"""
1.	Написать программу поиска самого длинного слова в строке, разделенной пробелами.
"""

while True:
    sentence = input("Введите строку, разделённую пробелами: ")

    # Разделение строки на слова и поиск самого длинного
    words = sentence.split()
    if words:  # Проверка, что строка не пуста
        longest_word = max(words, key=len)
        print(f"Самое длинное слово: {longest_word}")
        print(f"Его длина: {len(longest_word)} символов")
    else:
        print("Вы ввели пустую строку. Попробуйте ещё раз.")

    while True:
        retry = input("Хотите начать заново? (y/n): ").strip().lower()
        if retry in ['y', 'n']:
            break
        print("Некорректный ввод! Пожалуйста, введите 'y' для продолжения или 'n' для завершения.")

    if retry == 'n':
        print("Программа завершена. До свидания!")
        break