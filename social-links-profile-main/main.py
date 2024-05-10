import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Social-links")

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_coordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_coordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry(f"+{x_coordinate}+{y_coordinate-20}")

    root.mainloop()

