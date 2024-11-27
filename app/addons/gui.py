import tkinter as tk

def open_gui_window(categories):
    """Create a simple GUI window to display categories and websites."""
    window = tk.Tk()
    window.title("Web Launcher GUI")

    def show_websites(category):
        """Display the websites for a selected category."""
        websites = categories.get(category, [])
        for widget in frame.winfo_children():
            widget.destroy()
        
        for website in websites:
            label = tk.Label(frame, text=website, fg="blue", cursor="hand2")
            label.pack()
            label.bind("<Button-1>", lambda e, url=website: webbrowser.open(url))

    frame = tk.Frame(window)
    frame.pack()

    for category in categories:
        button = tk.Button(window, text=category, command=lambda cat=category: show_websites(cat))
        button.pack()

    window.mainloop()
