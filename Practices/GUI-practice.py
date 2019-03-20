from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.helloLabel = Label(self, text='This is my first GUI process')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='exit', command=self.quit)
        self.quitButton.pack()
app = Application()
app.master.title('Hello World')
app.mainloop()