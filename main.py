import sys
from threading import Thread
from time import sleep
from tkinter import Tk,N,E,W,S,BOTTOM,TOP,SOLID,RIGHT,LEFT,Y,X;
from tkinter.ttk import *;
from PyQt5.QtWidgets import QApplication;
import darkdetect,Style;

app = QApplication(sys.argv)

class MainApp:
    def __init__(self) -> None:
        self.thread=Thread(target=self.create)
        self.thread.start()
    def setTheme(self) -> None:
        try:
            if darkdetect.isDark():Style.set_theme("dark");
            else:Style.set_theme("light");
        except:Style.set_theme("dark");
    def buildWidgets(self):
        #Navigation Bar
        self.topBar = Frame(self.root)
        self.topBar.pack(side=TOP,fill=X)
    def onClose(self):
        for i in range(10):
            print(1-i/10)
            self.root.attributes("-alpha",1-(i/10))
            sleep(.01)
            self.root.update_idletasks()
        self.root.withdraw();
        sys.exit();
    def create(self):
        self.root=Tk();
        self.root.geometry("{}x{}".format(int(self.root.winfo_screenwidth()/3),int(self.root.winfo_screenheight()/3)));

        self.setTheme();
        self.buildWidgets();

        self.root.title("JSimple - 1.0")
        self.root.protocol("WM_DELETE_WINDOW",self.onClose)
        self.root.mainloop();

if __name__ == "__main__":
    MainApp()