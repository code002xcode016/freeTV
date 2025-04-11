import tkinter as tk
import mpv




root = tk.Tk()

frame = tk.Frame(root, width=700, height=600)
frame.pack()

display = tk.Frame(frame, bd=5)
display.place(relwidth=1, relheight=1)
#player.set_xwindow(display.winfo_id())
#player.set_nsobject(display.winfo_id())
player = mpv.MPV(log_handler=print , ytdl=True , wid=str(display.winfo_id()) , hwdec="auto")

player.play("/Users/hasrinismail/Downloads/freeetv/pyport/hachi.mp4")


root.mainloop()