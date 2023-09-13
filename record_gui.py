import tkinter as tk
import subprocess

def start_recording():
    subprocess.Popen(["arecord", "-d", "10", "-f", "cd", "-t", "wav", "-r", "16000", "-c", "1", "/tmp/recording.wav"])


def stop_recording():
    subprocess.Popen(["killall", "arecord"])


root = tk.Tk()

start_button = tk.Button(root, text="开始录音", command=start_recording)
start_button.pack()

stop_button = tk.Button(root, text="停止录音", command=stop_recording)
stop_button.pack()

root.mainloop()
