import tkinter as tk
from tkinter import ttk

from app.gui.barbers import BarbersTab

root = tk.Tk()
root.title("Симуляция парикмахерской")

tab_control = ttk.Notebook(root)

services_tab = ttk.Frame(tab_control)
tab_control.add(services_tab, text='Управление услугами')

barbers_tab = BarbersTab(tab_control)
tab_control.add(barbers_tab.frame, text='Управление парикмахерами')

clients_tab = ttk.Frame(tab_control)
tab_control.add(clients_tab, text='Симуляция клиентов')

stats_tab = ttk.Frame(tab_control)
tab_control.add(stats_tab, text='Статистика')

tab_control.pack(expand=1, fill="both")

root.mainloop()
