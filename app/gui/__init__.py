import tkinter as tk
from tkinter import ttk

from app.gui.barbers import BarbersTab
from app.gui.clients import ClientsTab
from app.gui.services import ServicesTab
from app.gui.statistics import StatisticsTab

root = tk.Tk()
root.title("Симуляция парикмахерской")

tab_control = ttk.Notebook(root)

services_tab = ServicesTab(tab_control)
tab_control.add(services_tab.frame, text='Управление услугами')

barbers_tab = BarbersTab(tab_control)
tab_control.add(barbers_tab.frame, text='Управление парикмахерами')

clients_tab = ClientsTab(tab_control)
tab_control.add(clients_tab.frame, text='Симуляция клиентов')

stats_tab = StatisticsTab(tab_control)
tab_control.add(stats_tab.frame, text='Статистика')

tab_control.pack(expand=1, fill="both")

root.mainloop()
