from pytube import YouTube
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk, filedialog
import os


def show_msg_wrapper(msg):
    def show_msg():
        mb.showinfo("Message", msg)

    return show_msg


def download(link, emplacement):
    youtube_object = YouTube(link)
    print(youtube_object.title)
    print(youtube_object.views)
    # youtube_object = youtube_object.streams.get_lowest_resolution()
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download(emplacement)
        show_msg_wrapper("Download completed")()
        if emplacement:
            os.startfile(emplacement)
    except:
        show_msg_wrapper("error")()


def choose_dir():
    # Open a directory chooser and get the selected directory's path
    dir_path = filedialog.askdirectory()

    # Set the text of button to the directory path
    button_choose_doc['text'] = dir_path


# creation de la frame
window = tk.Tk()
window.geometry("400x200")
window.title("youtube downloader")
# window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="white")

# creation des elements
link_label1 = tk.Label(window, text="Link", bg="white", font=("Century Gothic", 14))
text_link1 = tk.Text(window, height=1, font=("Century Gothic", 14), width=35, bg="white")
text_link2 = tk.Text(window, height=1, font=("Century Gothic", 14), width=35, bg="white")
link_label2 = tk.Label(window, text="File path", bg="white", font=("Century Gothic", 14))


def download_wrapper():
    # Get the values from the text widgets
    link = text_link1.get("1.0", "end-1c")
    emplacement = button_choose_doc['text']  # Get the file path from the button's text attribute

    # Call the download function with the values as arguments
    download(link, emplacement)


button_download = ttk.Button(text="download", command=download_wrapper)
button_choose_doc = tk.Button(text="Choose file", command=choose_dir)

# ajout des elements creer dans la frame
link_label1.grid(row=0, column=0, padx=2, pady=2)
text_link1.grid(row=1, column=0, padx=2, pady=2)
link_label2.grid(row=2, column=0, padx=2, pady=2)
button_choose_doc.grid(row=3, column=0, padx=2, pady=2)
button_download.grid(row=4, column=0, padx=2, pady=2)

if __name__ == '__main__':
    window.mainloop()
