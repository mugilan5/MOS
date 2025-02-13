import tkinter as tk
from tkinter import ttk

canvas = None
selected_tool = "pen"
selected_color = "black"
selected_size = 2
selected_pen_type = "line"
prev_x = None
prev_y = None

def setup_canvas(root):
    global canvas
    canvas_width = 800
    canvas_height = 600
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white", bd=3, relief=tk.SUNKEN)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def setup_navbar(root):
    navbar = tk.Menu(root)
    root.config(menu=navbar)

    file_menu = tk.Menu(navbar, tearoff=False)
    navbar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save Snapshot", command=take_snapshot)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    edit_menu = tk.Menu(navbar, tearoff=False)
    navbar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=undo)

def setup_tools(root):
    global selected_tool, selected_color, selected_size, selected_pen_type

    tool_frame = ttk.LabelFrame(root, text="Tools")
    tool_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.Y)

    pen_button = ttk.Button(tool_frame, text="Pen", command=select_pen_tool)
    pen_button.pack(side=tk.TOP, padx=5, pady=5)

    eraser_button = ttk.Button(tool_frame, text="Eraser", command=select_eraser_tool)
    eraser_button.pack(side=tk.TOP, padx=5, pady=5)

    brush_size_label = ttk.Label(tool_frame, text="Brush Size:")
    brush_size_label.pack(side=tk.TOP, padx=5, pady=5)

    brush_size_combobox = ttk.Combobox(tool_frame, values=[2, 4, 6, 8], state="readonly")
    brush_size_combobox.current(0)
    brush_size_combobox.pack(side=tk.TOP, padx=5, pady=5)
    brush_size_combobox.bind("<<ComboboxSelected>>", lambda event: select_size(int(brush_size_combobox.get())))

    color_label = ttk.Label(tool_frame, text="Color:")
    color_label.pack(side=tk.TOP, padx=5, pady=5)

    color_combobox = ttk.Combobox(tool_frame, values=["black", "red", "green", "blue", "yellow", "orange", "purple"], state="readonly")
    color_combobox.current(0)
    color_combobox.pack(side=tk.TOP, padx=5, pady=5)
    color_combobox.bind("<<ComboboxSelected>>", lambda event: select_color(color_combobox.get()))

    pen_type_label = ttk.Label(tool_frame, text="Pen Type:")
    pen_type_label.pack(side=tk.TOP, padx=5, pady=5)

    pen_type_combobox = ttk.Combobox(tool_frame, values=["line", "round", "square", "arrow", "diamond"], state="readonly")
    pen_type_combobox.current(0)
    pen_type_combobox.pack(side=tk.TOP, padx=5, pady=5)
    pen_type_combobox.bind("<<ComboboxSelected>>", lambda event: select_pen_type(pen_type_combobox.get()))

    clear_button = ttk.Button(tool_frame, text="Clear Canvas", command=clear_canvas)
    clear_button.pack(side=tk.TOP, padx=5, pady=5)

def setup_events():
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", release)

def select_pen_tool():
    global selected_tool
    selected_tool = "pen"

def select_eraser_tool():
    global selected_tool
    selected_tool = "eraser"

def select_size(size):
    global selected_size
    selected_size = size

def select_color(color):
    global selected_color
    selected_color = color

def select_pen_type(pen_type):
    global selected_pen_type
    selected_pen_type = pen_type

def draw(event):
    global prev_x, prev_y

    if selected_tool == "pen":
        if prev_x is not None and prev_y is not None:
            if selected_pen_type == "line":
                canvas.create_line(prev_x, prev_y, event.x, event.y, fill=selected_color,
                                    width=selected_size, smooth=True)
            elif selected_pen_type == "round":
                x1 = event.x - selected_size
                y1 = event.y - selected_size
                x2 = event.x + selected_size
                y2 = event.y + selected_size
                canvas.create_oval(x1, y1, x2, y2, fill=selected_color, outline=selected_color)
            elif selected_pen_type == "square":
                x1 = event.x - selected_size
                y1 = event.y - selected_size
                x2 = event.x + selected_size
                y2 = event.y + selected_size
                canvas.create_rectangle(x1, y1, x2, y2, fill=selected_color, outline=selected_color)
            elif selected_pen_type == "arrow":
                x1 = event.x - selected_size
                y1 = event.y - selected_size
                x2 = event.x + selected_size
                y2 = event.y + selected_size
                canvas.create_polygon(x1, y1, x1, y2, event.x, y2, fill=selected_color, outline=selected_color)
            elif selected_pen_type == "diamond":
                x1 = event.x - selected_size
                y1 = event.y
                x2 = event.x
                y2 = event.y - selected_size
                x3 = event.x + selected_size
                y3 = event.y
                x4 = event.x
                y4 = event.y + selected_size
                canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=selected_color, outline=selected_color)

        prev_x = event.x
        prev_y = event.y

def release(event):
    global prev_x, prev_y
    prev_x = None
    prev_y = None

def clear_canvas():
    canvas.delete("all")

def take_snapshot():
    canvas.postscript(file="snapshot.eps")

def undo():
    items = canvas.find_all()
    if items:
        canvas.delete(items[-1])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Paint")
    p1 = tk.PhotoImage(file = 'paint.png')
    root.iconphoto(False, p1)
    setup_canvas(root)
    setup_navbar(root)
    setup_tools(root)
    setup_events()

    root.mainloop()
