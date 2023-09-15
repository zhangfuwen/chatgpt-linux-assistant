import tkinter as tk

class ChatWindow:
    def __init__(self, callback=None):
        self.root = tk.Tk()
        self.root.title("Chat Window")

        self.chat_box = tk.Text(self.root, height=10, width=50)
        self.chat_box.pack()

        self.input_area = tk.Text(self.root, height=3, width=50)
        self.input_area.pack()
        self.input_area.bind("<Shift-Return>", self.handle_enter_key)
        self.input_area.bind("<Shift-Enter>", self.handle_enter_key)
        self.input_area.bind("<Return>", self.handle_enter_key)
        self.input_area.bind("<Enter>", self.handle_enter_key)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.callback=callback

    def handle_enter_key(self, event):
        self.send_message()

    def other_message(self, text):
        self.chat_box.insert(tk.END, f"{text}\n")

    def send_message(self):
        message = self.input_area.get("1.0", tk.END).strip()
        if message:
            self.chat_box.insert(tk.END, f"You: {message}\n")
            self.input_area.delete("1.0", tk.END)
            if self.callback:
                self.callback(message)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the ChatWindow class
    chat_window = ChatWindow()

    # Start the chat window application
    chat_window.run()