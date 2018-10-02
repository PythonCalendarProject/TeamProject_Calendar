from tkinter import *
from tkinter import ttk

class App_SettingDay_View:

    def __init__(self,parent):
        self.main_frame = Frame(parent)
        # 프레임 생성
        self.main_frame.pack()
        parent.geometry('400x400+350+250')
        parent.title("Day Setter")
        parent.resizable(False, False)
        parent.configure(background="white")

        self.main_container = Frame()
        self.main_container.pack(side=TOP)

        self.text=Text(parent, height=20, width=30)
        self.scroll = Scrollbar(parent, command=self.text.yview)

        self.text.configure(yscrollcommand=self.scroll.set)

        self.text.tag_configure('groove',
                           relief=GROOVE,
                           borderwidth=2)

        self.text.tag_bind('bite',
                      '<1>',
                      lambda e, t=self.text: t.insert(END, "Text"))
        self.text.pack(side=LEFT)
        self.scroll.pack(side=LEFT, fill=Y)

