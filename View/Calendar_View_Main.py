'''
VIEW GUI
made by KIM Myeong Jong, CHU Ho Jin, Yun Gun Hui, Park Un Che, Lee Sang Jin
start 2018-09-18 ~
if program was started than see this view
define main frame and framework
'''


from tkinter import *
from tkinter import ttk

from Controller import temp
from Controller import Calendar_Controller_dayClick

class App_Main_View:
    def __init__(self,parent):


        self.main_frame = Frame(parent)
        # 프레임 생성
        self.main_frame.pack()
        parent.geometry('1500x760+10+10')
        parent.title("Calendar")
        parent.resizable(False, False)
        parent.configure(background="white")

        #-------------------------------------------------------
        frame_padding = "2m"
        #-------------------------------------------------------

        self.main_container = Frame(background="white")
        self.main_container.pack()

        self.left_frame_schedule = Frame(self.main_container, background = "red", height=680,width=190)
        self.left_frame_schedule.pack(side=LEFT, fill=BOTH, padx=frame_padding, pady=frame_padding)
        # left frame        function schedule

        self.left_top_frame = Frame(self.left_frame_schedule, background = "pink", height=100, width=190)
        self.left_top_frame.pack(side=TOP, fill=BOTH)
        # left top frame    denote day of week

        self.right_frame_nav = Frame(self.main_container, background="blue", height=680, width=190)
        self.right_frame_nav.pack(side=RIGHT, padx=frame_padding, pady=frame_padding)
        # right frame       function navigation, wheather

        self.right_top_frame = Frame(self.right_frame_nav, background="green", height=100, width=190)
        self.right_top_frame.pack(side=TOP ,fill=BOTH)
        # right top frame   function/ weather

        self.right_bottom_frame = Frame(self.right_frame_nav, background="yellow", height=680, width=190)
        self.right_bottom_frame.pack(side=BOTTOM ,fill=BOTH)
        # right bottom frame    function navigation

        # self.right_bottom_Dday = Frame(self.right_bottom_frame, background="red", height=280, width=180)
        # self.right_bottom_Dday.pack(side=TOP)
        #
        # self.right_bottom_nav = Frame(self.right_bottom_frame, background="blue", height=280, width=180)
        # self.right_frame_nav.pack(side=BOTTOM)

        self.main_frame_calendar = Frame(self.main_container, background = "red", height=680,width=980)
        self.main_frame_calendar.pack(side=TOP, padx=frame_padding, pady=frame_padding)
        # main frame        function calendar

        self.main_frame_view_month = Frame(self.main_frame_calendar, background = "white", height=100, width=980)
        self.main_frame_view_month.pack(side=TOP, fill=BOTH)
        # main frame top    function view month

        self.main_frame_view_DOW = Frame(self.main_frame_view_month, background="yellow", height=20, width=1000)
        self.main_frame_view_DOW.pack(side=BOTTOM, fill=BOTH)

        for i in range(0,7):
            dayOfWeek = "";
            if (i==0):
                dayOfWeek="                 일                "
            elif (i==1):
                dayOfWeek="                월                 "
            elif (i==2):
                dayOfWeek="                 화                "
            elif (i==3):
                dayOfWeek="                 수                 "
            elif (i==4):
                dayOfWeek="                 목                "
            elif (i==5):
                dayOfWeek="                금                 "
            elif (i==6):
                dayOfWeek="                 토               "
            self.label_DOW= Label(self.main_frame_view_DOW,text=dayOfWeek)
            self.label_DOW.pack(side=LEFT, fill=BOTH)

        self.button_minus_month = Button(self.main_frame_view_month, width=2, height=2)
        self.button_minus_month.pack(side=LEFT)

        self.label_month = Label(self.main_frame_view_month, background = "white", height=2, width=40 ,text=str(temp.date_test_year)+"년 "+str(temp.date_test_month)+"월" ,font = "Helvetica 30 bold italic")
        self.label_month.pack(side=LEFT)

        self.button_plus_month = Button(self.main_frame_view_month, background="white",width=2,height=2)
        self.button_plus_month.pack(side=RIGHT)

        self.main_frame_view_day = Frame(self.main_frame_calendar, background = "gray", height=580, width=980)
        self.main_frame_view_day.pack(side=BOTTOM)
        # main frame bottom function view day [main]

        #--------------------delete-----------------------
        # font = font.Font()
        #-------------------------------------------------

        for i in range(0,6):
            for j in range(0,7):
                if (j==6):
                    self.button_main = Button(self.main_frame_view_day, width=7, height=2, background="gray99",
                                              foreground="BLUE", text="," + str(temp.date_test_start_point),
                                              font="Helvetica 25 bold italic", command=Calendar_Controller_dayClick.day_click).grid(row=i, column=j)
                elif(j==0):
                    self.button_main = Button(self.main_frame_view_day, width=7, height=2, background="gray99",
                                              foreground="red", text="," + str(temp.date_test_start_point),
                                              font="Helvetica 25 bold italic", command=Calendar_Controller_dayClick.day_click).grid(row=i, column=j)
                else:
                    self.button_main = Button(self.main_frame_view_day, width=7, height=2, background="gray99"
                                              ,foreground="black",text=","+str(temp.date_test_start_point),
                                              font = "Helvetica 25 bold italic", command=Calendar_Controller_dayClick.day_click).grid(row = i, column = j)

        self.main_frame.pack()

        # lbl.pack()
        # 패커 관리자 - 간단한 레이아웃을 최적화 시켜줌

test = Tk()
a = App_Main_View(test)
test.mainloop()
