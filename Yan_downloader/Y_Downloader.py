import pytube
from tkinter import *
from tkinter import ttk

def youTube_dwnld():
    try:    
        url_in = url_entry.get()
        res_in = str(res_entry.get())
        path = "C:"
        pytube.YouTube(url_in).streams.get_by_resolution(res_in).download(path)
    except AttributeError:
        pytube.YouTube(url_in).streams.get_lowest_resolution().download(path)
    
#def 

root = Tk()
root.title("youTube downloader")
root.iconbitmap("cosmic_cat1.ico")
root.geometry("480x320")


mainframe = ttk.Frame(root, padding="45 45 80 80")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

url = StringVar()
url_entry = ttk.Entry(mainframe, width=17, textvariable=url)
url_entry.grid(column=20, row=10, sticky=(W, E))

res = StringVar()
res_entry = ttk.Entry(mainframe, width=17, textvariable=res)
res_entry.grid(column=20, row=20, sticky=(W, E))

#meter = StringVar()
#ttk.Label(mainframe, textvariable=meter).grid(column=2, row=2, sticky=(W, E))

download_button = ttk.Button(mainframe, text="Download", command=youTube_dwnld).grid(column=30, row=60, sticky=W)
exit_button = ttk.Button(mainframe, text="Exit", command=mainframe.quit).grid(column=20, row=60, sticky=W)

#progress_bar = Progressbar(mainframe, orient=HORIZONTAL, lenght=300)

url_label = ttk.Label(mainframe, text="Input URL").grid(column=30, row=10, sticky=W)
res_label = ttk.Label(mainframe, text="Enter video res ('720p', '480p', '360p', '240p', '144p')").grid(column=30, row=20, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

url_entry.focus()
root.bind("<Return>", youTube_dwnld)

root.mainloop()

