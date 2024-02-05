import tkinter as tk
from tkinter import messagebox
import time


def sort_sequence():
    sequence = input_text.get("1.0", "end-1c").split(",")

    # Проверка наличия пустой строки в конце введенной последовательности
    if sequence[-1] == '':
        sequence = sequence[:-1]

    try:
        # Преобразование введенных значений в числа
        sequence = [int(num) for num in sequence]

        # Получение выбранного способа сортировки
        sort_method = sort_var.get()

        # Сортировка и замер времени
        start_time = time.time()

        if sort_method == "По возрастанию":
            sequence.sort()
        elif sort_method == "По убыванию":
            sequence.sort(reverse=True)

        end_time = time.time()

        # Вывод отсортированной последовательности и времени сортировки
        output_text.delete("1.0", "end")
        output_text.insert("1.0", str(sequence))

        elapsed_time = round(end_time - start_time, 4)
        messagebox.showinfo("Результат", f"Время сортировки: {elapsed_time} сек.")

    except ValueError:  # Обработка ошибки некорректного ввода
        messagebox.showerror("Ошибка", "Некорректный ввод. Введите числа через запятую.")


# Создание окна приложения
window = tk.Tk()
window.title("Сортировка чисел")
window.geometry("400x300")

# Создание поля ввода текста
input_label = tk.Label(window, text="Введите числа через запятую:")
input_label.pack()

input_text = tk.Text(window, height=1, width=30)
input_text.pack()

# Создание раскрывающегося списка
sort_label = tk.Label(window, text="Выберите способ сортировки:")
sort_label.pack()

sort_var = tk.StringVar()
sort_var.set("По возрастанию")

sort_option = tk.OptionMenu(window, sort_var, "По возрастанию", "По убыванию")
sort_option.pack()

# Создание кнопки Start
start_button = tk.Button(window, text="Start", command=sort_sequence)
start_button.pack()

# Создание поля вывода текста
output_text = tk.Text(window, height=10, width=30)
output_text.pack()

window.mainloop()