from tkinter import *
from tkinter import ttk

from View import Calendar_View_SettingDay

def day_click():
    print("1")
    test = Tk()
    a = Calendar_View_SettingDay.App_SettingDay_View(test)
    test.mainloop()