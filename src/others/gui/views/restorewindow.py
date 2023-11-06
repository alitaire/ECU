# import tkinter
# from tkinter.filedialog import askopenfilename
#
# class RestoreWindow(tkinter.Frame):
#     def __init__(self, master):
#         tkinter.Frame.__init__(self, master)
#         self._window = self.winfo_toplevel()
#         self._window.title("Restore")
#
#         btn_config = tkinter.Button(self._window, text="config.ini", command=self._open_file)
#         btn_config.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
#
#
#     def _open_file(self):
#         """Open a file for editing."""
#
#         self.filepath = askopenfilename(
#             filetypes=[("Config Files", "*.ini"), ("All Files", "*.*")]
#         )
#
#         if not self.filepath:
#             return
