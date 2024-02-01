import tkinter


class CreateToolTip:
    """ create a tooltip for a given widget """

    def __init__(self, widget, text: str = 'widget info'):
        self.waittime = 200  # time to wait before showing tooltip (milliseconds)
        self.wraplength = 180  # max length in pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)  # bind functions to actions
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        # position of tooltip: next to widget (right hand side) -> no problems at overlapping area:
        x += self.widget.winfo_rootx() + self.widget.winfo_width()
        y += self.widget.winfo_rooty()
        # creates a toplevel window
        self.tw = tkinter.Toplevel(self.widget)  # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(self.tw, text=self.text, justify='left',
                              background="#ffffff", relief='solid', borderwidth=1,
                              wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
