from tkinter import *
from tkinter import ttk
from fuzzywuzzy import fuzz

def fuzzy_deduplicate(bullet_points, threshold, progress_bar, progress_var):
    """
    Takes a list of bullet points and returns a deduplicated list of bullet points
    using fuzzy string matching.
    """
    deduplicated_points = []
    num_duplicates = 0
    for i, point in enumerate(bullet_points):
        if not any(fuzz.token_set_ratio(point, p) >= threshold for p in deduplicated_points):
            deduplicated_points.append(point)
        else:
            num_duplicates += 1
        progress = (i + 1) / len(bullet_points)
        progress_var.set(progress)
        root.update()
    return deduplicated_points, num_duplicates


def convert_bullet_points():
    threshold_value = threshold_var.get()
    if threshold_value == '':
        threshold_value = 100
    threshold = int(threshold_value)
    input_text = input_box.get("1.0", END).strip()
    bullet_points = input_text.split("\n")
    progress_var.set(0)
    deduplicated_points, num_duplicates = fuzzy_deduplicate(bullet_points, threshold, progress_bar, progress_var)
    output_text = "\n".join([f"- {p.strip('- ')}" for p in deduplicated_points])
    output_box.delete("1.0", END)
    output_box.insert(END, output_text)
    num_duplicates_label.config(text=f"{num_duplicates} duplicates found")
    progress_var.set(100)

# Create GUI
root = Tk()
root.title("Fuzzy Markdown List Deduplication")
root.minsize(width=400, height=200)
root.configure(background='#111111')

# variable for threshold value
threshold_var = StringVar()

# Set style for dark theme
style = ttk.Style()
style.theme_use('clam')
style.configure('.', background='#111111', foreground='#00ffff')
style.configure('TButton', background='#333333', foreground='#00ffff', lightcolor='#555555')
style.configure('TLabel', background='#111111', foreground='#00ffff')
style.configure('TEntry', background='#222222', foreground='#00ffff')
style.map('TEntry', background=[('readonly', '#222222')])

# Create input box
input_box = Text(root, height=10, width=1, bg='#222222', fg='#00ffff', insertbackground='#00ffff')
input_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
input_box_width = root.winfo_width() * 0.45
input_box.config(width=int(input_box_width))

# Create convert button
convert_button = ttk.Button(root, text="Deduplicate List Items", command=convert_bullet_points)
convert_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
convert_button_width = root.winfo_width() * 0.1
convert_button.config(width=int(convert_button_width))
style.map('TButton', background=[('active', '#555555')])

# # Create output box
# output_box = Text(root, height=10, width=1, bg='#222222', fg='#00ffff', insertbackground='#00ffff')
# output_box.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
# output_box_width = root.winfo_width() * 0.45
# output_box.config(width=int(output_box_width))

# Create threshold frame
threshold_frame = Frame(root, bg='#111111')
threshold_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Create threshold label
threshold_label = ttk.Label(threshold_frame, text="Threshold -", background='#111111', foreground='#00ffff')
threshold_label.grid(row=0, column=0, sticky="w")

# Create threshold entry box
threshold_var = StringVar()
threshold_box = ttk.Entry(threshold_frame, width=5, justify="center", background='#222222', foreground='#000000')
threshold_box.insert(END, "90")
threshold_box.grid(row=0, column=1, sticky="w")

# Create threshold percent label
threshold_percent_label = ttk.Label(threshold_frame, text=" % similarity", background='#111111', foreground='#00ffff')
threshold_percent_label.grid(row=0, column=2, sticky="w")

# Set column proportions
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=1)

# Set row proportions
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)

# Create output box
output_box = Text(root, height=1, width=1, bg='#222222', fg='#00ffff', insertbackground='#00ffff')
output_box.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
output_box_width = root.winfo_width() * 0.45
output_box.config(width=int(output_box_width))

# Create progress bar
progress_var = DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

# Create label for displaying number of duplicates found
num_duplicates_label = ttk.Label(root, text="", background='#111111', foreground='#00ffff')
num_duplicates_label.grid(row=3, column=2, sticky="se", padx=10, pady=10)

# Bind update function to output box
def on_configure(event):
    output_box.yview_moveto(0)

output_box.bind('<Configure>', on_configure)

# Run main event loop
root.mainloop()
