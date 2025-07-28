import tkinter as tk
from tkinter import messagebox, filedialog
from yt_dlp import YoutubeDL
import os

def download_audio():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Keine URL", "Bitte gib eine YouTube-URL ein.")
        return

    # Zielordner auswählen
    output_dir = filedialog.askdirectory(title="Zielordner wählen")
    if not output_dir:
        return

    # YT-DLP Optionen
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Erfolg", "Download abgeschlossen! MP3 gespeichert in:\n" + output_dir)
    except Exception as e:
        messagebox.showerror("Fehler", f"Download fehlgeschlagen:\n{e}")

# GUI aufbauen
root = tk.Tk()
root.title("YouTube -> MP3 Downloader")
root.geometry("450x150")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill='both')

url_label = tk.Label(frame, text="YouTube-Link:")
url_label.grid(row=0, column=0, sticky='w')

url_entry = tk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=(5, 0))
url_entry.focus()

download_btn = tk.Button(frame, text="Herunterladen als MP3", command=download_audio)
download_btn.grid(row=1, column=0, columnspan=2, pady=(10,0))

root.mainloop()


