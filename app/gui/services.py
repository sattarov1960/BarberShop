import tkinter as tk
from tkinter import ttk, messagebox

from app import barber_shop


class ServicesTab:
    def __init__(self, tab_control):
        self.frame = ttk.Frame(tab_control)
        self.services = []
        self.setup_widgets()
        self.load_service()

    def setup_widgets(self):
        # Setting up the service list Treeview
        self.tree = ttk.Treeview(self.frame, columns=('name', 'cost', 'time', 'category'), show='headings')
        self.tree.heading('name', text='Название услуги')
        self.tree.heading('cost', text='Стоимость')
        self.tree.heading('time', text='Время (мин)')
        self.tree.heading('category', text='Категория')

        # Align text to the left for all columns
        self.tree.column('name', anchor='w')  # Set text alignment to west (left) for the name column
        self.tree.column('cost', anchor='w')  # Set text alignment to west (left) for the cost column
        self.tree.column('time', anchor='w')  # Set text alignment to west (left) for the time column
        self.tree.column('category', anchor='w')  # Set text alignment to west (left) for the category column

        self.tree.pack(side='left', fill='both', expand=True)

        # Add fields for new service on the right
        entry_frame = ttk.Frame(self.frame)
        entry_frame.pack(side='right', fill='y', padx=20)

        ttk.Label(entry_frame, text="Название услуги:").pack(pady=5)
        service_options = ['Painting nails', 'Coloring', 'Shave', 'Haircut']
        self.service_name_combobox = ttk.Combobox(entry_frame, values=service_options)
        self.service_name_combobox.pack(pady=5)

        ttk.Label(entry_frame, text="Категория услуги:").pack(pady=5)
        service_options = ['basic', 'standard', 'complex', 'non-standard']
        self.service_category_combobox = ttk.Combobox(entry_frame, values=service_options)
        self.service_category_combobox.pack(pady=5)

        ttk.Label(entry_frame, text="Стоимость услуги:").pack(pady=5)
        self.service_cost_entry = ttk.Entry(entry_frame)
        self.service_cost_entry.pack(pady=5)

        ttk.Label(entry_frame, text="Время выполнения (мин):").pack(pady=5)
        self.service_time_entry = ttk.Entry(entry_frame)
        self.service_time_entry.pack(pady=5)

        add_service_button = ttk.Button(entry_frame, text="Добавить услугу", command=self.add_service)
        add_service_button.pack(pady=20)

    def load_service(self):
        for service in barber_shop.getServices():
            data = (service.get_name(), service.get_price(), service.get_duration(), service.get_category())
            self.services.append(data)
            self.tree.insert('', 'end', values=data)

    def add_service(self):
        # Логика для добавления услуги
        name = self.service_name_combobox.get()
        category = self.service_category_combobox.get()
        cost = self.service_cost_entry.get()
        time = self.service_time_entry.get()

        if name in [i.get_name() for i in barber_shop.getServices()]:
            messagebox.showerror("Ошибка", "Данный тип услуги уже существует!")
            return
        if not all([cost.isdigit(), time.isdigit()]):
            messagebox.showerror("Ошибка", "Не соответсвует тип данных!")
            return
        if name and cost and time and category:
            # Добавление услуги в список и обновление Treeview
            self.services.append((name, cost, time, category))
            self.tree.insert('', 'end', values=(name, cost, time, category))
            messagebox.showinfo("Успех", f"Услуга '{name}' добавлена!")
            self.service_name_combobox.set('')
            self.service_category_combobox.set('')
            self.service_cost_entry.delete(0, tk.END)
            self.service_time_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
