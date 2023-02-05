import tkinter
import customtkinter
from pytube import YouTube

def start_download(): 
  try:
    ytLink = link.get()
    ytObject = YouTube(ytLink, on_progress_callback=on_progress)

    # video
    print('getting high resolution video')
    video = ytObject.streams.get_highest_resolution()

    # update title
    title.configure(text=ytObject.title)
    finish_label.configure(text='')

    #download video
    video.download()
    finish_label.configure(text='Downloaded!', text_color='black')
  except:
    finish_label.configure(text='Download Error', text_color='red')


def on_progress(stream, chunk, bytes_remaining): 
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining

  #calc percent completed
  percentage_of_completion = bytes_downloaded / total_size * 100
  percent = str(int(percentage_of_completion))
  percentage.configure(text=percent + '%')
  percentage.update()

  #update progress bar
  progressBar.set(float(percentage_of_completion) / 100)


# System Settings Defaults
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# App frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Youtube Download')


# UI Elements
title = customtkinter.CTkLabel(app, text="Insert A Youtuke Link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress percentage
percentage = customtkinter.CTkLabel(app, text='0%')
percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text='Download', command=start_download)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()